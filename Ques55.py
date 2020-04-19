# Write a program for converting weight from Pound to Kilo grams.
# a) Use assertion for the negative weight.
# b) Use assertion to weight more than 100 KG

def PoundToKg(pound):
  try:
    assert (pound>=0),"Negative weight not allowed"
    return pound*0.453592

  except AssertionError as exp:
      return exp
print(PoundToKg(43))
print(PoundToKg(-13))

def PoundToKg(pound):
  try:
    assert (pound>=100), "Weight should be more than or equal to 100"
    return pound*0.453592
  except AssertionError as exp:
      return exp
print(PoundToKg(56))
print(PoundToKg(101))