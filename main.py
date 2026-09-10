from pyscript import document

VAT_PERCENT = 0.12

def generate_receipt(event):
    beef = document.getElementById("item1")
    pork = document.getElementById("item2")
    birria = document.getElementById("item3")
    fish = document.getElementById("item4")
    chicken = document.getElementById("item5")

    subtotal_cost = (
        float(beef.value) * beef.checked
        + float(pork.value) * pork.checked
        + float(birria.value) * birria.checked
        + float(fish.value) * fish.checked
        + float(chicken.value) * chicken.checked
    )

    # Compute tax and grand total
    vat_cost = subtotal_cost * VAT_PERCENT
    final_cost = subtotal_cost + vat_cost

    receipt_template = f"""
    <div>
        <h3>Order Receipt</h3>
        <p>Subtotal: ₱{subtotal_cost:.2f}</p>
        <p>VAT (12%): ₱{vat_cost:.2f}</p>
        <p><strong>Total Amount: ₱{final_cost:.2f}</strong></p>
    </div>
    """

    document.getElementById("receipt_display").innerHTML = receipt