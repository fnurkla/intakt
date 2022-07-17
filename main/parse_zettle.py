# Used to generate the JSON-object from the Zettle API respnose.

from datetime import datetime
import argparse
import get_zettle_purchases


def parse(data, time_delta):
    print("time delta =", time_delta)
    print("data =", data)
    return


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-sd",
        "--start-date",
        help="The start date for the fetch of Zettle sales. Date is on ISO format: yy-mm-ddThh:mm:ss, time is default to zero",
    )

    parser.add_argument(
        "-ed",
        "--end-date",
        default=None,
        nargs="?",
        help="The end date for the fetch of Zettle sales, same format as start_date",
    )

    parser.add_argument(
        "-td",
        "--time-delta",
        default="daily",
        nargs="?",
        help="The time of which each report spans",
    )

    args = vars(parser.parse_args())

    print(args)
    start_date = datetime.fromisoformat(args["start_date"])
    end_date = datetime.fromisoformat(args["end_date"]) if args["end_date"] is not None else None
    time_delta = args["time_delta"]

    sales = get_zettle_purchases.get_sales(start_date, end_date)
    return parse(sales, time_delta)


if __name__ == "__main__":
    main()
