class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        line_length = 0
        words_setup = []
        result = []
        words_leftover = []
        
        while words:
            for word in words:
                if len(word) == maxWidth and len(words_setup)==0:
                    result.append(word)
                else:
                    line_length += len(word) + 1
                    words_setup.append(word)
                    if line_length - 1 > maxWidth:
                        
                        print(words_setup)
                        while line_length > maxWidth:
                            print('yes1 line > width')
                            if line_length - 1 <= maxWidth:
                                line_length -= 1
                            else:
                                line_length -= len(words_setup[-1])+1
                                words_leftover.insert(0, words_setup[-1])
                                words_setup.pop()
                        print(words_setup)
                        print('ending')
                        line_length_space = len(''.join(words_setup)) + len(words_setup) - 1
                        while line_length_space > maxWidth:
                            print('yes222 line > width')
                            line_length_space -= len(words_setup[-1])+1
                            words_leftover.insert(0, words_setup[-1])
                            words_setup.pop()
                        print(words_setup)
                        print('ending2')
                        if len(words_setup) == 1:
                            line_result = words_setup[0] + ' ' * (maxWidth - len(words_setup[0]))
                            result.append(line_result)
                        elif ((maxWidth - len(''.join(words_setup))) % (len(words_setup) - 1) == 0) and len(words_setup) > 1:
                            num_of_spaces_bet_words = (maxWidth - len(''.join(words_setup))) // (len(words_setup) - 1)
                            line_result = words_setup[0] + ''.join([(' '*num_of_spaces_bet_words + str(word)) for word in words_setup[1:]])
                            result.append(line_result)
                        else:
                            num_of_places = len(words_setup) - 1
                            num_of_spaces = maxWidth - len(''.join(words_setup))
                            spaces = [' '*(num_of_spaces//num_of_places)] * num_of_places
                            rem = num_of_spaces % num_of_places
                            for idx in range(rem):
                                spaces[idx] += ' '
                            line_result = words_setup[0]
                            idx = 0
                            for word in words_setup[1:]:
                                line_result += (spaces[idx] + word)
                                idx += 1
                            result.append(''.join(line_result))
                        
                        line_length = len(''.join(words_leftover))
                        words_setup = words_leftover
                        words_leftover = []
                
                #print(result)
            words = words_setup
            words_setup = []
            line_length = 0

            if words and (len(''.join(words))+len(words)-1 <= maxWidth):
                result_last = words[0]
                for word in words[1:]:
                    result_last += ' '+word
                
                result_last += ' '*(maxWidth-len(result_last))
                result.append(result_last)
                words = []
        
        return result