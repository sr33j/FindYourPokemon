from random import choice
import requests
from bs4 import BeautifulSoup

def get_pokemon(gen):
	html_doc = requests.get(
		"https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number").text
	soup = BeautifulSoup(html_doc, 'html.parser')
	pokeTables = soup.find_all('table')
	firstGen = pokeTables[gen]
	links = firstGen.find_all('a')

	for link in links:
		if "(Pokémon)" in link['title']:
			print(link.get_text())

#taken from https://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/
def edit_dist_recur(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
 
    # Fill d[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
 
            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j
 
            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i
 
            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 
            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = min(1+dp[i][j-1],        # Insert
                               1+dp[i-1][j],        # Remove
                               1+dp[i-1][j-1])    # Replace
 
    return dp[m][n]

def edit_dist(str1, str2):
	return edit_dist_recur(str1, str2, len(str1), len(str2))

def find_close_pokemon(name):
	min_dist = 1000000
	your_pokemon = []
	for gen in range(1,4):
		f = open("pokemon"+str(gen)+".txt")
		for line in f:
			dist = edit_dist(name, line.strip().lower())*1.0/len(line.strip())
			if dist < min_dist:
				your_pokemon = [line.strip().lower()]
				min_dist = dist
			elif dist == min_dist:
				your_pokemon.append(line.strip().lower())
	return list(set(your_pokemon))


def commonPrefixLength(str1, str2):
	length = 0
	for i in range(len(str1)):
		if str1[i] == str2[i]:
			length+=1
		else:
			break
	return length

def closest_prefix(name, closePokemon):
	prefixLen = 0
	your_pokemon = []
	for pokemon in closePokemon:
		match = commonPrefixLength(name, pokemon)
		if match > prefixLen:
			your_pokemon = [pokemon]
			prefixLen = match
		elif match == prefixLen:
			your_pokemon.append(pokemon)
	return your_pokemon

def closest_length(name, closePokemon):
	min_diff = 1000000
	your_pokemon = []
	for pokemon in closePokemon:
		diff = abs(len(name)-len(pokemon))
		if diff < min_diff:
			your_pokemon = [pokemon]
			min_diff = diff
		elif diff == min_diff:
			your_pokemon.append(pokemon)
	return your_pokemon

def find_your_pokemon(name):
	name = name.lower()

	closePokemon = find_close_pokemon(name)
	if len(closePokemon) == 1:
		return closePokemon[0]
	else:
		closePokemon = closest_prefix(name, closePokemon)

	if len(closePokemon) == 1:
		return closePokemon[0]
	else:
		closePokemon = closest_length(name, closePokemon)

	if len(closePokemon) == 1:
		return closePokemon[0]
	else:
		return choice(closePokemon)
