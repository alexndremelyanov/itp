def separated_print(input_fn):
    def output_fn():
        print("--------------")
        input_fn()
        print("--------------")
    return output_fn

