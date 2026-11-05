"""Statistics helpers."""
"""Statistics for a list of marks."""
def average(marks):
	return sum(marks) / len(marks)
def highest (marks):
	return max(marks)
def lowest(marks):
	return min(marks)
def pass_count(marks, pass_mark):
	read pass_mark from .env instead of the caller
	count = 0 
	for marks in mark:
		if marks >= pass_mark
