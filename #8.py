__author__ = 'Nafiul Islam'
__title__ = 'Largest product in a series'
from functools import reduce
from operator import mul

var = "7316717653133062491922511967442657474235534919493496983520312774506326239578318" \
      "0169848018694788518438586156078911294949545950173795833195285320880551112540698747158523" \
      "8630507156932909632952274430435576689664895044524452316173185640309871112172238311362229" \
      "8934233803081353362766142828064444866452387493035890729629049156044077239071381051585930" \
      "7960866701724271218839987979087922749219016997208880937766572733300105336788122023542180" \
      "9751254540594752243525849077116705560136048395864467063244157221553975369781797784617406" \
      "4955149290862569321978468622482839722413756570560574902614079729686524145351004748216637" \
      "0484403199890008895243450658541227588666881164271714799244429282308634656748139191231628" \
      "2458617866458359124566529476545682848912883142607690042242190226710556263211111093705442" \
      "1750694165896040807198403850962455444362981230987879927244284909188845801561660979191338" \
      "7549920052406368991256071760605886116467109405077541002256983155200055935729725716362695" \
      "61882670428252483600823257530420752963450"

m = max(reduce(mul, map(int, ns))
        for ns in zip(var[:], var[1:], var[2:], var[3:], var[4:]))
print(m)