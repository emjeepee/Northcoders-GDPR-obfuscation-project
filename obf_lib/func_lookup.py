from obf_lib.deal_with_csv import deal_with_csv
from obf_lib.deal_with_json import deal_with_json
from obf_lib.deal_with_parquet import deal_with_parquet


# make function lookup table:
func_lookup = {
    "csv": deal_with_csv,
    "json": deal_with_json,
    "parquet": deal_with_parquet,
}
