def analyse_postcode(postcode):
    import csv,os
    file_path=os.getcwd()+"\\\data\\\pp-2022.csv"
    pp2022=[]
    prices=0
    minimum_price=float("inf")
    minimum_price_property=""
    maximum_price=0
    maximum_price_property=""
    postcode=postcode.upper()
    try:
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[3][:len(postcode)]==postcode:
                    prices+=int(row[1])
                    pp2022.append(row)
                    if float(row[1])<minimum_price:
                        minimum_price_property="-".join(row)
                        minimum_price=int(row[1])
                    if float(row[1])>maximum_price:
                        maximum_price_property="-".join(row)
                        maximum_price=int(row[1])
        if pp2022:
            num_sold=len(pp2022)
            average_price=int(prices/num_sold)
            results={
                     "num_sold":num_sold,
                     "average_price":average_price,
                     "minimum_price":minimum_price,
                     "minimum_price_property":minimum_price_property,
                     "maximum_price":maximum_price,
                     "maximum_price_property":maximum_price_property}
        else:
            return None
        return results
    except Exception:
        print(Exception)
