from argparse import ArgumentParser

def get_args():
    parser.add_argument(
        "--file_name",
        "-file",
        default="test_data.txt",
        help="The name of file containing input. Default: test_data.txt")
    return parser.parse_args()