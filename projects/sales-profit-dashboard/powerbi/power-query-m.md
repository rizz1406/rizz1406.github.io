# Power Query M — Cleaning steps (paste in Advanced Editor)

```m
let
    Source = Csv.Document(File.Contents("data/raw/sales_superstore_raw.csv"), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    Promoted = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    Typed = Table.TransformColumnTypes(Promoted, {
        {"Order Date", type date}, {"Ship Date", type date},
        {"Sales", type number}, {"Quantity", Int64.Type},
        {"Discount", type number}, {"Profit", type number}
    }),
    Trimmed = Table.TransformColumns(Typed, {}, Text.Trim),
    Filtered = Table.SelectRows(Trimmed, each [Sales] > 0 and [Discount] >= 0 and [Discount] <= 0.8),
    AddedMargin = Table.AddColumn(Filtered, "Margin", each [Profit]/[Sales], type number)
in
    AddedMargin
```

Save cleaned output to `data/processed/sales_cleaned.csv`.
