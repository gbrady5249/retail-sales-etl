# Data Dictionary

## UCI Online Retail Dataset

| Column | Description | Expected Type |
|---|---|---|
| InvoiceNo | Unique invoice number. Invoice numbers beginning with "C" indicate cancellations. | String |
| StockCode | Unique product/item identifier. | String |
| Description | Product description. | String |
| Quantity | Number of items purchased. Negative values represent returns/cancellations. | Integer |
| InvoiceDate | Date and time of the transaction. | Datetime |
| UnitPrice | Price per item. | Decimal |
| CustomerID | Unique customer identifier. Missing for some transactions. | Integer/Nullable |
| Country | Customer's country. | String |

## Dataset Statistics

- Rows: 541,909
- Unique invoices: 25,900
- Unique products: 4,070
- Unique customers: 4,372
- Countries: 38
- Start date: December 1, 2010
- End date: December 9, 2011

## Known Data Quality Issues

- 1,454 missing product descriptions
- 135,080 missing CustomerID values
- 5,268 duplicate rows
- 10,624 rows with negative quantities
- 9,288 rows with cancellation invoice numbers
- 2 rows with negative unit prices

## Data Engineering Notes

Missing values and unusual transactions will be investigated
before transformation. Records will not be removed without
establishing a business rule for their treatment.