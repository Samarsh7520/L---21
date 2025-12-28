code =  { "India": "0091",
         "Australia": "0061",
         "United Kingdom": "044",
         "United States": "001",
         "Germany": "0049",
         "France": "033",
         "China":"0086"}

print("India Code:", code.get("India", "Not Found"))
print("Japan Code:", code.get("Japan","Not Found"))
print("China Code:", code.get("China","Not Found"))
print("United States Code:", code.get("United States","Not Found"))