ric_cusip_mapper={
    "IBM.N":"US4592001014",
    "TRIL.L":"GB00B29MWZ99",
    "Future derivative":"DE000C0JK7R7",
    "Bond":"DE0001135317",
    "Bond":"DE0001135"
}

print(ric_cusip_mapper["IBM.N"])
print(ric_cusip_mapper.get("TRIL.L"))
print(ric_cusip_mapper.get("ED","Euro doller"))
print(ric_cusip_mapper.get("Bond"))
