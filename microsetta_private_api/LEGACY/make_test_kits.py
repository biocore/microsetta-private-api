import string
import random
import datetime
import uuid
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.api.tests.test_integration import \
    _create_mock_kit


def make_test_kits(output_filename=None, num_kits=100,
                   samples_lower_limit=1, samples_upper_limit=5):

    # Ugh, imports are here inside this function because transaction
    # (and thus test_integration, which depends on transaction)
    # requires that an ag_test db *already* exist. Thus we can't
    # import it without an error until after the rest of the code
    # (outside this function) actually creates that database ...


    if output_filename is None:
        output_filename = "test_kit_ids_" + datetime.datetime.now().strftime(
            "%Y%m%d%H%M%S") + ".csv"

    # right now I don't want to deal with the complication of how to ensure
    # that as we increment the base barcode, we don't go into >9 digits, so
    # I am putting this arbitrary and low limit on it for now.
    if num_kits > 1000:
        raise ValueError("make_test_kits is not able to create more than 1000"
                         "test kits")
    base_barcode = 999010000
    curr_barcode = base_barcode

    external_kit_ids = []

    with Transaction() as t:
        for curr_kit_num in range(0, num_kits):
            # generate a mock internal kit id and a mock human-readable kit id
            curr_kit_id = str(uuid.uuid4())
            curr_external_kit_id = generate_random_kit_name()
            external_kit_ids.append(curr_external_kit_id)

            # select a random number of swabs to add to this kit;
            # upper limit is plus 1 bc randrange stop argument is exclusive
            curr_num_samples = random.randrange(samples_lower_limit,
                                                samples_upper_limit+1)

            # make barcodes/sample ids for swabs to be added to this mock kit
            barcodes = []
            mock_sample_ids = []
            for curr_sample_index in range(0, curr_num_samples):
                mock_sample_ids.append(str(uuid.uuid4()))
                barcodes.append(curr_barcode)
                curr_barcode += 1
            # next barcode/sample to create ids for

            # create the mock kit with all the specified mock barcodes/
            # samples
            _create_mock_kit(t, barcodes, mock_sample_ids,
                             curr_kit_id, curr_external_kit_id)
        # next kit to create

        t.commit()
    # end transaction

    # create a file of the kit names
    with open(output_filename, 'w') as filehandle:
        filehandle.write('%s\n' % "kit_id")
        for curr_external_kit_id in external_kit_ids:
            filehandle.write('%s\n' % curr_external_kit_id)

    print("created {0} test kits with {1}-{2} samples each".format(
        num_kits, samples_lower_limit, samples_upper_limit))
    print("kit names in {0}".format(output_filename))


def generate_random_kit_name(name_length=8, name_base="test"):
    letters_and_digits = string.ascii_letters + string.digits
    rand_name = ''.join(random.choice(letters_and_digits)
                        for i in range(name_length))
    return rand_name + name_base


make_test_kits()
