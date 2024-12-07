from pathlib import Path
import polars as pl


def main():
    with open(Path.joinpath(Path(__file__).parent, "input.txt")) as _file:
        data = {"col_1": [], "col_2": []}
        for line in _file:
            stripped = line.strip().replace(" ", ",").split(",")
            first, last = stripped[0], stripped[-1]
            (data["col_1"].append(int(first)))
            data["col_2"].append(int(last))

        sorted_df = pl.Series("col_1", data["col_1"]).sort(descending=True).to_frame()
        sorted_df = sorted_df.with_columns(
            pl.Series("col_2", data["col_2"]).sort(descending=True)
        )
        final_val = sorted_df.with_columns(
            (pl.col("col_1") - pl.col("col_2")).abs().alias("distance")
        ).sum().item(0, "distance")

        print(f"final value is : {final_val}")


if __name__ == "__main__":
    main()
