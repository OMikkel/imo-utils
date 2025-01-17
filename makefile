build:
	cython main.py --embed
	gcc -Os $(python3-config --includes) main.c -o imo-utils $(python3-config --ldflags --embed)