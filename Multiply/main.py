def main(args):
	val1 = args.get("val1", 1)
	val2 = args.get("val2", 1)
	return { "val1" : val1, "val2" : val2, "result" : val1 * val2 }
