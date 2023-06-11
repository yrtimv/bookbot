import collections
import sys


def count_words(s: str) -> int:
  return len(s.split())


def count_letters(s: str) -> dict[str, int]:
  letters = collections.defaultdict(lambda: 0)
  for l in s:
    if l.isalpha():
      letters[l.lower()] += 1
  return letters


def main():
  args = sys.argv[1:]
  if len(args) == 0:
    print('No file defined.')
    exit()

  filename = args[0]
  with open(filename) as file:
    contents = file.read()

  words = count_words(contents)
  letters = count_letters(contents)
  sorted_letters = sorted(letters, key=lambda x: letters[x], reverse=True)

  print(f'--- Begin report of {filename} ---')
  print(f'{words} words found in the document')

  for l in sorted_letters:
    print(f'The \'{l}\' character was found {letters[l]} times')


main()
