def SpectralConvolution(spectrum):
    result = []
    for i in range(len(spectrum)):
        for j in range(i + 1, len(spectrum)):
            if abs(spectrum[j]-spectrum[i]) != 0:
                result.append(abs(spectrum[j]-spectrum[i]))
    return result



spectrum = "0 86 160 234 308 320 382"
spectrum = spectrum.split(" ")
spectrum = [int(i) for i in spectrum]
a = sorted(SpectralConvolution(spectrum))

from collections import Counter
print Counter(a)
print [i for i in a if (i>=57) and (i<=200)]
