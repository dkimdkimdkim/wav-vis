#!/usr/bin/python

<<<<<<< HEAD
"""
WAV specification:
00---------------
  | ChunkID         0x52494646 (RIFF)      BigEndian
04---------------
  | ChunkSize
08---------------
  | Format          0x57415645 (WAVE)      BigEndian
12---------------
  | Subchunk1 ID                           BigEndian
16---------------
  | Subchunk1 Size
20---------------
  | AudioFormat
22---------------
  | NumChannels
24---------------
  | SampleRate
28---------------
  | ByteRate
32---------------
  | BlockAlign
34---------------
  | BitsPerSample
36---------------
  | Subchunk2 ID
40---------------
  | Subchunk2 Size
44---------------
  | data
"""

import binascii
import io
import struct
import collections

WAV_HEADER = 'RIFF'
FIELD_CONSTANTS = collections.OrderedDict([   # value is (size in bytes, is little_endian?)
    ('chunkid'        , (4, False)),
    ('chunksize'      , (4, True)),
    ('format'         , (4, False)),
    ('subchunk1id'    , (4, False)),
    ('subchunk1size'  , (4, True)),
    ('audioformat'    , (2, True)),
    ('numchannels'    , (2, True)),
    ('samplerate'     , (2, True)),
    ('byterate'       , (4, True)),
    ('blockalign'     , (2, True)),
    ('bitspersample'  , (2, True)),
    ('subchunk2id'    , (4, False)),
    ('subchunk2size'  , (4, True)),
    ])

NUMERIC_CONSTANTS = {
    'chunksize',
    'subchunk1size',
    'audioformat',
    'numchannels',
    'samplerate',
    'byterate',
    'blockalign',
    'bitspersample',
    'subchunk2size'
    }

class WavInfo:
    field_constant_values = {}
    data = []

wav_info = WavInfo()

""" Reads metainformation about the WAV file into the global Data class.
    Leaves stream pointer at start of DATA blocks.
   """
def parse_header(stream):
    # Seek to beginning of file.
    stream.seek(0)

    stream_position = 0
    for field_name, field_value in FIELD_CONSTANTS.items():
        stream_value = stream.read(field_value[0])
        print type(stream_value)
        byte = b'0x0'
        if field_value[1]:
            byte = struct.unpack('<%dB' % (field_value[0]), stream_value.decode('utf-8'))
        else:
            byte = struct.unpack('>%dB' % (field_value[0]), binascii.hexlify(stream_value))
        if field_name in NUMERIC_CONSTANTS:
            #int(''.join(reversed(byte)).encode('hex'), 16)
            wav_info.field_constant_values[field_name] = int(byte.encode('hex'), 16)
        else:
            wav_info.field_constant_values[field_name] = byte

def parse_data_chunk(stream):
    while stream.peek():
        byte = stream.read(wav_info.field_constant_values['bitspersample'] / 8)
        byte = byte[::-1]
        wav_info.data.append(int(byte.encode('hex'), 16))

srcfile = "helloworld.wav"
f = io.open(srcfile, "r+b")

nBytes = 1
nChunks = 4

parse_header(f)
print wav_info.field_constant_values
parse_data_chunk(f)

sample_index = 0
for sample in wav_info.data:
    print str(sample_index) + ',' + str(sample)
    sample_index += 1

"""
while f.peek():
    hex_line = ''
    for i in range(4):
        hex_line += ' ' + binascii.hexlify(f.read(nBytes))
    print str(file_offset) + ':' + hex_line
    file_offset += 4
"""
