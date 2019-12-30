from fourier import FourierApp
import functions
from helper import parse_args, parser

dict_names = dict((name, f) for name, f in functions.__dict__.items() if callable(f))

def get_func(name):
    return dict_names.get(name, functions.power_func)


if __name__ == '__main__':
    args = parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        print('Possible function names : {}'.format(dict_names.keys()))
        FourierApp(func=get_func(args.func), n=args.n, k=args.k).run()
