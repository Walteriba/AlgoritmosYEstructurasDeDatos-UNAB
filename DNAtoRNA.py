# CONVERTIDOR DE ADN A ARN A MI FORMA
# GCAT => GCAU
x = input(" Ingrese su cadena de DNA en MAYUSCULAS ")
dna = list(x)
arn = []
for base in dna:
    if (base == "T"):
        arn.append("U")  # .append agrega lo que esta adentro a la lista
    else:
        arn.append(base)
strarn = "".join(arn)  # uno la lista en un string
print("Su cadena de ARN es: ", (strarn))

#CONVERTIDOR DE ADN A ARN OPTIMO CODEWARS
def dna_to_rna(dna):
    return dna.replace('T', 'U')





