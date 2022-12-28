import win32com.client
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer

# Create an instance of the QuickBooks Application object
qb = win32com.client.Dispatch("QBXMLRP2e.RequestProcessor")

print(qb)
# Connect to QuickBooks
qb.OpenConnection("", "QuickBooks Integrator")
qb.BeginSession("", 0)

# Modify an item in the item list
item_xml = """
<ItemInventoryAddRq>
  <ItemInventoryAdd>
    <Name>dawa1</Name>
    <SalesOrPurchase>
      <SalesAndPurchase>
        <SalesPrice>20</SalesPrice>
        <PurchaseCost>15</PurchaseCost>
      </SalesAndPurchase>
    </SalesOrPurchase>
  </ItemInventoryAdd>
</ItemInventoryAddRq>

"""
response = qb.ProcessRequest(item_xml)

# Disconnect from QuickBooks
qb.EndSession()
qb.CloseConnection()
