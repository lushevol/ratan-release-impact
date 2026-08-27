# Title
[Settlement] Rebook enhancement

# Description
Considering currently there is no linkage between original cashflow and the replacement, RATAN put the control to prevent duplicate payments:
When a new cashflow came, it will be tagged as "Rebook" if any cashflow RELEASED in VD-5 Need to consider more accurate way of identifying it.
Current Behavior:
 • limit to 5 days
 • limit to same ccy
Future Behavior:
 • additional limit to Payment Type
