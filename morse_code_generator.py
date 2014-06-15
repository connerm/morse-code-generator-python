#!/usr/bin/python

import sys
import wave

def main():
  print "Morse Code Generator - arg1->text to convet arg2-> outfile name (use .wav)"
  text = sys.argv[1]
  text = text.lower() 
  print "Text: " + text


  infiles = ["dot.wav", "dash.wav"]
  outfile = sys.argv[2]
  print "Outfile: " + outfile
  
  code = {
    'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....',
    'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
    'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
    'y':'-.--', 'z':'--..', '9':'.----', '0':'-----', '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'....-', '7':'...--', '8':'..---', '.':'.-.-.-', ',':'--..--',
    ':':'---...', '?':'..--..', '\'':'.----.', '-':'-....-', '/':'-..-.', '{':'-.--.-',
    '}':'-.--.-', '\"':'.-..-.', '@':'.--.-.', '=':'-...-',' ':' ' 
  }

  morse = ""
  for letter in text:
    morse += code[letter] + " "
  print "Morse Code: " + morse

  data= []
  for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append( [w.getparams(), w.readframes(w.getnframes())] )
    w.close()
  
  dot = wave.open(infiles[0], 'rb')
  frameLength = len(dot.readframes(1)) * 7
  space = '\x00' * frameLength

  output = wave.open(outfile, 'wb')
  output.setparams(data[0][0])
  for point in morse:
    if point == '.':
      output.writeframes(data[0][1])
    if point == '-':
      output.writeframes(data[1][1])
    if point == ' ':
      output.writeframes(space)
  output.close()
	

if __name__ == "__main__":
  main()
