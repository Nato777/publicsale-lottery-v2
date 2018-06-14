import secrets


def main():

    target_number = 1500

    with open('./airbloc-publicsale-lottery-input.txt', 'r') as f:

        # load input file and make it list
        extracted_list = f.readlines()

        # randomly choice
        rand = secrets.SystemRandom()
        winners_list = rand.sample(extracted_list, k=target_number)

        check_duplicate(winners_list)

        # write result to file
        with open('./airbloc-publicsale-lottery-result.txt', 'w') as fw:
            fw.writelines(winners_list)

        print("Done!")

def check_duplicate(winners_list):

    if len(winners_list) != len(list(set(winners_list))):
        raise Exception('Duplicated element on the list!')

if __name__ == '__main__':
    main()
