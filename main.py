from datetime import datetime

import pandas as pd
import yaml


def get_data(file_path: str):
    return pd.read_csv(file_path)


def filter_data(columns: list, data_frame, report):

    for header in columns:
        for col, conf in header.items():
            if "default_null" in conf:
                data_frame[col].fillna(conf["default_null"], inplace=True)

            if not conf["empty"]:
                data_frame = data_frame[data_frame[col].notna()]

            if conf["type"] == "date":
                if "default_null" in conf:
                    data_frame[col].fillna(datetime.now(), inplace=True)
                else:
                    data_frame[col] = data_frame[col].replace(conf["separator"], "")
                    data_frame[col] = pd.to_datetime(data_frame, format=conf["format"])
            else:
                data_frame[col] = data_frame[col].astype(conf["type"])

                if "min_len" in conf:
                    data_frame = data_frame[
                        data_frame.apply(
                            lambda x: len(x[col]) >= conf["min_len"], axis=1
                        )
                    ]
                if "max_len" in conf:
                    data_frame = data_frame[
                        data_frame.apply(
                            lambda x: len(x[col]) <= conf["max_len"], axis=1
                        )
                    ]
                if "unique" in conf:
                    data_frame.drop_duplicates(subset=[col])

    if report == "vendas_itens":
        data_frame["valor_total"] = (
            data_frame["valor_unitario"] * data_frame["quantidade_produto"]
        )

    return data_frame


if __name__ == "__main__":
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    df_filtered = []

    for key, value in config["files"].items():
        raw_data = get_data(value["path"])
        df_filtered.append(filter_data(value["columns"], raw_data, key))

    with pd.option_context(
        "display.max_rows",
        None,
        "display.max_columns",
        None,
    ):
        for df in df_filtered:
            print(df)
