import sys
import app.t_w as tw
import app.state_leaders_spider as sls

def main(args=None):
    if args is None:
        args = sys.argv[1:]
	tw.main('leaders.txt')
	#sls.main()

if __name__ == '__main__':
    main()
