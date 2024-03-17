def calcular_descuento(monto_total):

  if (monto_total >= 150):
    por_descuento =20
    descuento = (monto_total * por_descuento)/100
  elif (monto_total >= 100):
    por_descuento = 10
    descuento = (monto_total * por_descuento)/100
  else:
    descuento = 0
  return descuento

monto_total1 = float(input("Ingrese el monto total de la primera compra: "))

monto_total2 = float(input("Ingrese el monto total de la segunda compra: "))
descuento1 = calcular_descuento(monto_total1)
descuento2 = calcular_descuento(monto_total2)
monto_final1 = monto_total1 - descuento1
monto_final2 = monto_total2 - descuento2
print(f"-----------------------------------")
print(f"Monto total de la primera compra: {monto_total1:.2f}")
print(f"Descuento: {descuento1:.2f}")
print(f"Monto total a pagar: {monto_final1:.2f}")
print(f"-----------------------------------")
print(f"Monto total de la segunda compra: {monto_total2:.2f}")
print(f"Descuento: {descuento2:.2f}")
print(f"Monto total a pagar: {monto_final2:.2f}")
