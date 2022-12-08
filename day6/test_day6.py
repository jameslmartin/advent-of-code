from day6 import scan


def test_scan_for_packets():
    case_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    case_2 = "nppdvjthqldpwncqszvftbrmjlhg"
    case_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    case_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    
    packet_window_size = 4

    result_1 = scan(case_1, packet_window_size)
    result_2 = scan(case_2, packet_window_size)
    result_3 = scan(case_3, packet_window_size)
    result_4 = scan(case_4, packet_window_size)
    
    assert result_1 == 5
    assert result_2 == 6
    assert result_3 == 10
    assert result_4 == 11

def test_scan_for_messages():
    case_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" 
    case_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" 
    case_3 = "nppdvjthqldpwncqszvftbrmjlhg"
    case_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    case_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

    message_window_size = 14

    result_1 = scan(case_1, message_window_size)
    result_2 = scan(case_2, message_window_size)
    result_3 = scan(case_3, message_window_size)
    result_4 = scan(case_4, message_window_size)
    result_5 = scan(case_5, message_window_size)
    
    assert result_1 == 19
    assert result_2 == 23
    assert result_3 == 23
    assert result_4 == 29
    assert result_5 == 26