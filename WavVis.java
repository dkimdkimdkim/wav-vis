/*
    david m kim
    copyright 2014.
*/

/***************

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

******************/

public class WavVis
{
    private static final String WAV_HEADER = "RIFF";
    private static final FIELD_CONSTANTS = collections.OrderedDict([   // value is (size in bytes, is little_endian)
        ("chunkid"        , (4, False)),
        ("chunksize"      , (4, True)),
        ("format"         , (4, False)),
        ("subchunk1id"    , (4, False)),
        ("subchunk1size"  , (4, True)),
        ("audioformat"    , (2, True)),
        ("numchannels"    , (2, True)),
        ("samplerate"     , (2, True)),
        ("byterate"       , (4, True)),
        ("blockalign"     , (2, True)),
        ("bitspersample"  , (2, True)),
        ("subchunk2id"    , (4, False)),
        ("subchunk2size"  , (4, True)),
        ])

    private static final HashSet<String> NUMERIC_CONSTANTS = new HashSet<String>(new String[] {
        "chunksize",
        "subchunk1size",
        "audioformat",
        "numchannels",
        "samplerate",
        "byterate",
        "blockalign",
        "bitspersample",
        "subchunk2size"
    });

    public class WavInfo {
    }
        field_constant_values = {}
        data = []
    public static void main(String[] args)
    {
        
    }
}
