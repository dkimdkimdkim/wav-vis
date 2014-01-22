#!/usr/bin/python

import io
import binascii

WAV_HEADER = 'RIFF'
FIELD_CONSTANTS = {
    'CHUNK_ID' : 4,
    'CHUNK_SIZE' : 4,
    'FORMAT' : 4,
    'DATA_OFFSET' : 44
    }

def parse_header(stream):
  # Keep track of original stream position.
  original_pos = stream.tell()

  # Seek to beginning of file.
  stream.seek(0)

  chunk_id = stream.read(FIELD_CONSTANTS['CHUNK_ID'])

  if not chunk_id == WAV_HEADER:
    raise Exception('File is not WAV formatted.')

  chunk_size = stream.read(FIELD_CONSTANTS['CHUNK_SIZE'])

  # Return to original stream position.
  stream.seek(original_pos)
  descriptor_data = {
      'CHUNK_SIZE' : chunk_size
      }
  return descriptor_data

def seek_to_data(stream):
  stream.seek(FIELD_CONSTANTS['DATA_OFFSET'])

srcfile = "helloworld.wav"
f = io.open(srcfile, "r+b")

nBytes = 1

print parse_header(f)
seek_to_data(f)

print '------ DATA'

nChunks = 4

file_offset = FIELD_CONSTANTS['DATA_OFFSET']

while f.peek():
  hex_line = ''
  for i in range(4):
    hex_line += ' ' + binascii.hexlify(f.read(nBytes))
  print str(file_offset) + ':' + hex_line
  file_offset += 4
