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

        count = 0
        df = pl.DataFrame(data["col_2"]).group_by("column_0").len().sort("len", descending=True)
        for row in df.iter_rows():
            if row[0] in data["col_1"]:
                count += row[0] * row[1]

        print(f"Final count is : {count}")
                

if __name__ == "__main__":
    main()
