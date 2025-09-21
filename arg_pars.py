import argparse

def main():
    parser = argparse.ArgumentParser(description="cli demo")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_greet = sub.add_parser("greet", help="say hi")
    p_greet.add_argument("name")

    p_add = sub.add_parser("add", help="add a + b")
    p_add.add_argument("-a", type=int, required=True)
    p_add.add_argument("-b", type=int, required=True)

    args = parser.parse_args()
    if args.cmd == "greet":
        print(f"hello {args.name}")
    if args.cmd == "add":
        print(args.a / args.b)


if __name__ == "__main__":
    main()