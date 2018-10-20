def main(args):
	val1 = args.get("val1", 0)
	val2 = args.get("val2", 0)
	result = val1 + val2
	print(result)
	return {"val1" : val1, "val2" : val2, "result" : result, "name" :  "result: " + str(result)}
