debug = True
filename = "main.m"

def help ():
	print("\n--- Help for M ---")
	print("To define a function:")
	print("    f(a,b) = a + b")
	print("To use conditions:")
	print("    f(a,b) = a if a > b else b")
	print("To take user input (supports float, int, str)")
	print("    a <- int <- Enter an int")

def main():
	lines = open(filename).readlines()
	line = ""
	for line in lines:
		line = line.strip()
		if (line == "" or line == "exit" or "//" in line):
			continue
		if (line == "help"):
			help()
			continue
		parts = line.split("(")
		if ("<-" in line):
			parts = line.split("<-")
			print(parts[2].strip())
			usrin = raw_input()
			opt = parts[1].strip()
			if (opt == "int"):
				pass
			elif (opt == "float"):
				pass
			elif (opt == "str"):
				usrin = "'" + usrin + "'"
			else:
				print("Syntax error in line " + line)
				print("Non-supported data type entered")
			ex = parts[0].strip() + " = " + usrin
			exec (ex, globals())
			continue
		if ("=" not in line):
			exec ("print(" + line + ")")
		elif ((" if " in line) and (" else " in line)):
			ex = "def "
			parts = line.split("=")
			ex += parts[0].replace(" ","")
			ex += ":\n"
			if (debug):
				ex += " print(\"" + parts[0].replace(" ", "") + "\", " + line.split("(")[1].split(")")[0] + ")\n"
			conditions = line.split(" if ")[1].split(" else ")
			ex += " if(" + conditions[0] + "):\n"
			ex += "  return (" + parts[1].split(" if ")[0].replace(" ","") + ")\n"
			ex += " else:\n"
			ex += "  return (" + conditions[1].replace(" ","") + ")\n"

			exec(ex, globals())
		else:
			ex = "def "
			parts = line.split("=");
			ex += parts[0].replace(" ", "")
			ex += ":\n"
			if (debug):
				ex += " print(\"" + parts[0].replace(" ", "") + "\", " + line.split("(")[1].split(")")[0] + ")\n"
			ex += " return (" + parts[1].replace(" ", "") + ")\n"
				
			exec(ex, globals())

main()
