import re
from random import seed
from random import randint
from datetime import datetime

ARRAYSIZE_MAX = 6000
ASCII_SPACE = 32
ASCII_DEL = 127

class Travesty:
    def __init__(self, buffer_size,
          pattern_length,
          out_chars,
          line_width,
          use_verse,
          debug,
          input_file):

        self.buffer_size = buffer_size
        self.pattern_length = pattern_length
        self.out_chars = out_chars
        self.line_width = line_width
        self.use_verse = use_verse
        self.debug = debug
        self.input_file = input_file

        self.freq_array = []
        self.start_skip = []
        for i in range(0, ASCII_DEL+1):
            self.freq_array.append(0)
            self.start_skip.append(0)

        self.skip_array = []
        for i in range(0, buffer_size+1):
            self.skip_array.append(0)


        #self.skip_array.append(ARRAYSIZE_MAX)
        self.pattern = ""
        self.char_count = 0
        self.near_end = False

    # FreqArray is indexed by 93 probable ASCII characters, from ASCII_SPACE to ASCII_DEL.
    # Its elements are all set to zero.
    def clear_freq_array(self):
        for ch in range(ASCII_SPACE, ASCII_DEL+1):
            self.freq_array[ch]=0

    # Reads input_file from disk into buffer_array, cleaning it up and reducing any run of
    # whitespace to a single space.  (If no inputfile is supplied stdin is used instead)
    # Once read it then copies to end of array a string of its opening characters as long
    # as the pattern_length, in effect wrapping the end to the beginning.
    def fill_array(self):
        if not self.input_file:
            try:
                print("Reading from stdin...");
                self.buffer = sys.stdin.readlines()
            except:
                "ERROR: Something went wrong reading from stdin"
        else:
            print(f"Reading from: {self.input_file}...");
            with open(self.input_file, 'r') as file:
                self.buffer = file.read().replace('\n', ' ')

        buffer_array_tmp = re.sub('(\s{2,}|\n)',' ', self.buffer.strip())
        self.buffer_array = buffer_array_tmp[0:self.buffer_size-(self.pattern_length + 1)] + ' ' + buffer_array_tmp[0:self.pattern_length]

        seed(datetime.now())

        print(f"Characters read, plus wraparound = {len(self.buffer_array)}")

    # User selects "order" of operation, an integer, n, in the range 1 .. 9. The input
    # text will henceforth be scanned in n-sized chunks. The first n-1 characters of the
    # input file are placed in the "Pattern" Array. The Pattern is written at the head of output.
    def first_pattern(self):
        self.pattern = self.buffer_array[0:self.pattern_length]
        self.char_count = self.pattern_length
        self.near_end = False
        if self.use_verse:
            print(' ', end='') # Align first line
        print(f"{self.pattern}", end='')

    # The i-th entry of skip_array contains the smallest index j < i such that
    # buffer_array[O] = buffer_array[i]. Thus skip_array links together all identical characters
    # in buffer_array.  start_skip contains the index of the first occurrence of each
    # character, These two arrays are used to skip the matching routine through the
    # text, stopping only at locations whose character matches the first character
    # in Pattern.
    def init_skip_array(self):
        for ch in range(ASCII_SPACE, ASCII_DEL+1):
            self.start_skip[ch] = len(self.buffer_array)

        for j in range(len(self.buffer_array), 0, -1):
            ch = ord(self.buffer_array[j-1:j]);
            self.skip_array[j-1] = self.start_skip[ch];
            self.start_skip[ch] = j;

    # Checks buffer_array for strings that match Pattern; for each match found, notes
    # following character and increments its count in FreqArray. Position for first
    # trial comes from StartSkip; thereafter positions are taken from SkipArray.
    # Thus no sequence is checked unless its first character is already known to
    # match first character of Pattern.
    def match_pattern(self):
        ch = ord(self.pattern[0:1])
        i = self.start_skip[ch] - 1;        # i is 1 to left of the Match start
        while i <= (len(self.buffer_array) - self.pattern_length - 1) and i >= 0:
            if self.buffer_array[i:i+self.pattern_length] == self.pattern:
                next_char_val = ord(self.buffer_array[i + self.pattern_length: i + self.pattern_length + 1])
                self.freq_array[next_char_val] += 1
            i = self.skip_array[i] - 1

    # It is chosen at Random from characters accumulated in FreqArray during
    # last scan of input.
    def get_next_char(self):
        total = 0
        for ch in range(ASCII_SPACE, ASCII_DEL+1):
            total = total + self.freq_array[ch] # Sum counts in FreqArray

        assert total > 0, f"Error: Pattern Match not found."
        toss = randint(1, total);
        counter = ASCII_SPACE - 1;
        while toss > 0:
            counter += 1
            if toss > self.freq_array[counter]:
                toss = toss - self.freq_array[counter];
            else:
                toss = 0;
        return chr(counter)

    # The next character is written.  Output lines will
    # average self.line_width characters in length. If "Verse" option has been selected,
    # a new line will commence after any word that ends with "'"in input file.
    # Thereafter lines will be indented until the self.line_width-character average has
    # been made up.
    def write_character(self, char):
        char_val=ord(char)
        if char_val != ASCII_DEL:
            print(f"{char}", end='');

        self.char_count = self.char_count + 1
        if self.char_count % self.line_width == 0:
            self.near_end = True
        if self.use_verse and char_val == ASCII_DEL:
            print("")
        if self.near_end and char_val == ASCII_SPACE:
            print("")
            if self.use_verse:
                print("   ")
            self.near_end = False

    # This removes the first character of the Pattern and appends the character
    # just printed. FreqArray is zeroed in preparation for a new scan.
    def new_pattern(self, char):
        self.pattern = self.pattern[1:self.pattern_length] + char
        self.clear_freq_array();

    def output_debug_info(self, show_buffer, show_buffer_array):
        print(f"buffer_size={self.buffer_size} ", end='')
        print(f"pattern_length={self.pattern_length} ", end='')
        print(f"out_chars={self.out_chars} ", end='')
        print(f"input_file={self.input_file} ", end='')
        print(f"buffer Size={len(self.buffer)} ", end='')
        print(f"buffer_array Size={len(self.buffer_array)} ", end='')
        print("\n");
        if show_buffer:
            print(f"Buffer Data:\n{self.buffer}\n")

        if show_buffer_array:
            print(f"buffer_array:\n{self.buffer_array}\n")

    def execute(self):
        self.clear_freq_array()
        self.fill_array()

        if self.debug:
            self.output_debug_info(False, False)

        self.first_pattern()
        self.init_skip_array()

        next_char = ' '
        while (self.char_count < self.out_chars or next_char != ' '):
            self.match_pattern()
            next_char = self.get_next_char()
            assert len(next_char) > 0, f"ERROR: Unable to find next character."
            self.write_character(next_char)
            self.new_pattern(next_char)

        print("")
        print("")
        print(f"Output: {self.char_count} characters.")
