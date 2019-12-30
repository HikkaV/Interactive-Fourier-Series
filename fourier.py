from symfit import parameters, variables, sin, cos, Fit
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation


class FourierApp:
    sns.set()

    def __init__(self, func, low_lim=-np.pi, high_lim=np.pi, n=3, figsize=(15, 12), k=5):
        if n>10:
            print('Calculating fourier series for more than 10 items is inefficient')
        self.func_name = func.__name__
        self.n = n
        self.k = k
        self.func = func
        self.low_lim = low_lim
        self.high_lim = high_lim
        self.fig = plt.figure(figsize=figsize)
        self.xdata, self.ydata = self.make_data()
        plt.plot(self.xdata, self.ydata)
        self.initial, = plt.plot([], [], color="blue")
        self.initial.set_data(self.xdata, self.ydata)
        self.fourier, = plt.plot([], [], color="red", ls=':')
        Writer = animation.writers['pillow']
        writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

    def animate(self, i):
        plt.title('Fourier series for {0} with {1} elements'.format(self.func_name, i + 1))
        y = self.app(i)
        self.fourier.set_data(self.xdata, y)
        return self.fourier,

    def init(self):
        self.fourier.set_data([], [])
        return self.fourier,

    def fourier_series(self, x, f, n=2):
        a0, *cos_a = parameters(','.join(['a{}'.format(i) for i in range(0, n + 1)]))
        sin_b = parameters(','.join(['b{}'.format(i) for i in range(1, n + 1)]))
        series = a0 + sum(ai * cos(i * f * x) + bi * sin(i * f * x)
                          for i, (ai, bi) in enumerate(zip(cos_a, sin_b), start=1))
        return series

    def make_data(self):
        xdata = np.linspace(self.low_lim, self.high_lim)
        if self.func_name == 'power_func':
            ydata = self.func(xdata, k=self.k)
        else:
            ydata = self.func(xdata)
        return xdata, ydata

    def app(self, n):
        n = n + 1
        x, y = variables('x, y')
        w, = parameters('w')
        model_dict = {y: self.fourier_series(x, f=w, n=n)}
        fit = Fit(model_dict, x=self.xdata, y=self.ydata)
        fit_result = fit.execute()
        return fit.model(x=self.xdata, **fit_result.params).y

    def run(self):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init,
                                       frames=self.n, blit=False, repeat=True, save_count=50)
        plt.show()
        anim.save(self.func_name+'_fourier_fit.gif',writer='pillow')
