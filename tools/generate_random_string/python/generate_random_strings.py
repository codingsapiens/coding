import string
import random
import strgen

def pw_gen(size, generator_condition):
	generated_random_string = ''.join(random.choice(generator_condition) for _ in range(size))
	if any(char.isdigit() for char in generated_random_string) == True:
		return generated_random_string
	else:
		print("#"*30,"\nNo number :", generated_random_string,"\nRegenerate random string.") 
		while any(char.isdigit() for char in generated_random_string) == False:
			generated_random_string = ''.join(random.choice(generator_condition) for _ in range(size))
			return generated_random_string

def random_generator():
	generated_random_string = strgen.StringGenerator("[\d\w]{12}").render()
	return generated_random_string

if __name__ == "__main__":
	print("#"*30,"\npw_gen : ", pw_gen(8, string.ascii_lowercase + string.digits + string.ascii_uppercase),"\n")
	print("#"*30,"\nrandom_generator : ", random_generator(),"\n")
