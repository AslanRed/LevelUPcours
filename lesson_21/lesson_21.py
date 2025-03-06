import argparse

# parser = argparse.ArgumentParser(description = 'Proces some integers')
# parser.add_argument('num1', type = int, help = 'The first number to add.')
# parser.add_argument('num2', type = int, help = 'The second number to add.')

# parser.add_argument('-v', '--verbose', action = 'store_true', help  = 'Increase output verbosity.')
# args = parser.parse_args()

# result = args.num1 + args.num2
# print('The sum of {} and {} is {}'.format(args.num1, args.num2, result))

# if args.verbose:
#     print('Verbose is enabled')

# parser = argparse.ArgumentParser(description = 'Process multiple files.')
# parser.add_argument('filenames', nargs = '+', help = 'List of files to process.')
# args = parser.parse_args()
# for filename in args.filename:
#     print(f'Processing file: {filename}')
#     #Add your fule processing code

# parser =argparse.ArgumentParser(description = 'Peerform actions in different modes')
# parser.add_argument('--mode', choices = ['backup', 'restore', 'delete'], required = True, help = 'Mode of operation')
# args = parser.parse_args()
# if args.mode == 'backup':
#     print('Backing up data')
# elif args.mode == 'restore':
#     print('restoring data')
# elif args.mode == 'delete':
#     print('deleting data')

parser = argparse.ArgumentParser()
parser.add_argument('num1', type = float, help = 'first nuber')
parser.add_argument('num2', type = float, help = 'second nuber')
parser.add_argument('operator', choices=['-', '+', '*', '/'])
args = parser.parse_args()
if args.operator == '-':
    result = args.num1 - args.num2
elif args.operator == '+':
    result = args.num1 + args.num2
elif args.operator == '*':
    result = args.num1 * args.num2
elif args.operator == '/':
    if args.num2 == 0:
        print('You cannot devide number by zero')
    else:
        result = args.num1 / args.num2
print(f'{result}')