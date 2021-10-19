import json
from flask import Response
from unittest.mock import patch
from microsetta_private_api.repo.transaction import Transaction
from microsetta_private_api.admin.daklapack_polling import \
    process_order_articles, poll_dak_orders
from microsetta_private_api.repo.admin_repo import AdminRepo
from microsetta_private_api.admin.tests.test_admin_repo import AdminTests


def make_test_response(status_code, json_dict):
    result = Response(response=json.dumps(json_dict) + "\n",
                      status=status_code,
                      mimetype='application/json')
    return result


class DaklapackPollingTests(AdminTests):
    ARTICLES_INFO = {"articles": [
        {"articleCode": "350201",
         "total": 2,
         "new": 0,
         "inProduction": 0,
         "sent": 2,
         "errors": 0,
         "articles": [
             {"internalId": "729f7149-4889-42b3-8368-1b68284d5b95",
              "articleCode": "350201",
              "status": "Sent",
              "description": "A test description",
              "sendInformation": {
                  "firstName": "Natalia J Phillips", "lastName": "",
                  "address1": "2166  Chapmans Lane", "insertion": "",
                  "address2": "", "postalCode": "88103", "city": "Clovis",
                  "state": "NM", "country": "USA", "countryCode": "US",
                  "phone": "505-784-5252", "companyName": "Jane Doe"
              },
              "shippingProvider": {
                  "name": "FedEx", "shippingType": "FEDEX_2_DAY"
              },
              "scannableKitItems": [
                  {"type": "Tube", "barcode": "ABCT",
                   "creationDate": "2021-02-26T08:48:16.788439Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "KitId", "barcode": "ABCR",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "BoxId", "barcode": "ABCX",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "Form", "barcode": "ABCF",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "Tube", "barcode": "ABCN",
                   "creationDate": "2021-02-26T08:48:16.788439Z",
                   "itemCount": 1,
                   "containerItems": []
                   }
              ],
              "inBoundDelivery": {"code": "Tracking Code 2"},
              "outBoundDelivery": {"code": "Tracking Code 1"},
              "code": None, "plannedSendDate": None
              },
             {"internalId": "9e07e45b-c302-4f8a-b040-21b30d6b28e0",
              "articleCode": "350201",
              "status": "Sent",
              "description": None,
              "sendInformation": {
                  "firstName": "Natalia J Phillips", "lastName": "",
                  "address1": "2166  Chapmans Lane", "insertion": "",
                  "address2": "", "postalCode": "88103", "city": "Clovis",
                  "state": "NM", "country": "USA", "countryCode": "US",
                  "phone": "505-784-5252", "companyName": "Jane Doe"
              },
              "shippingProvider": {
                  "name": "FedEx", "shippingType": "FEDEX_2_DAY"
              },
              "scannableKitItems": [
                  {"type": "Tube", "barcode": "ABCT2",
                   "creationDate": "2021-02-26T08:48:16.788439Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "KitId", "barcode": "ABCR2",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "BoxId", "barcode": "ABCX2",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "Form", "barcode": "ABCF2",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "Tube", "barcode": "ABCN2",
                   "creationDate": "2021-02-26T08:48:16.788439Z",
                   "itemCount": 1,
                   "containerItems": []
                   }
              ],
              "inBoundDelivery": None,
              "outBoundDelivery": {"code": "Tracking Code 2"},
              "code": None, "plannedSendDate": None
              }  # end article instance
         ]},  # end "articles" (instance) list, single article (type) entry
        {"articleCode": "350100",
         "total": 1,
         "new": 0,
         "inProduction": 0,
         "sent": 1,
         "errors": 0,
         "articles": [
             {"internalId": "8abf7149-4889-42b3-8368-1b68284d5b95",
              "articleCode": "350100",
              "status": "Sent",
              "description": None,
              "sendInformation": {
                  "firstName": "Natalia J Phillips", "lastName": "",
                  "address1": "2166  Chapmans Lane", "insertion": "",
                  "address2": "", "postalCode": "88103", "city": "Clovis",
                  "state": "NM", "country": "USA", "countryCode": "US",
                  "phone": "505-784-5252", "companyName": "Jane Doe"
              },
              "shippingProvider": {
                  "name": "FedEx", "shippingType": "FEDEX_2_DAY"
              },
              "scannableKitItems": [
                  {"type": "KitId", "barcode": "DEFR",
                   "creationDate": "2021-02-26T08:48:16.788439Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "Tube", "barcode": "DEFT",
                   "creationDate": "2021-02-26T08:48:16.7885478Z",
                   "itemCount": 1,
                   "containerItems": []
                   },
                  {"type": "BoxId", "barcode": "DEFX",
                   "creationDate": "2021-02-26T08:48:16.788439Z",
                   "itemCount": 1,
                   "containerItems": []
                   }
              ],
              "inBoundDelivery": None,
              "outBoundDelivery": None,
              "code": None, "plannedSendDate": None
              }  # end article instance
         ]}  # end "articles" (instance) list, single article (type) entry
    ]}  # end "articles" (type) list, outer dict

    @staticmethod
    def _delete_dak_orders_to_kits(t, kit_ids):
        if kit_ids is None:
            kit_ids = []

        kit_ids_tuple = tuple(kit_ids)
        with t.dict_cursor() as cur:
            cur.execute("DELETE FROM barcodes.daklapack_order_to_kit "
                        "USING barcodes.kit "
                        "WHERE "
                        "daklapack_order_to_kit.kit_uuid = kit.kit_uuid "
                        "AND kit.kit_id IN %s",
                        (kit_ids_tuple,))

    @staticmethod
    def _delete_kits(t, kit_ids):
        if kit_ids is None:
            kit_ids = []

        with t.dict_cursor() as cur:
            for curr_kit_id in kit_ids:
                # Delete from ag-kit-related tables if it
                # was added there
                cur.execute("SELECT ag_kit_id "
                            "FROM ag.ag_kit "
                            "WHERE supplied_kit_id=%s",
                            (curr_kit_id,))
                ag_kit_ids_fetch = cur.fetchall()

                if len(ag_kit_ids_fetch) > 0:
                    ag_kit_ids = ag_kit_ids_fetch[0]

                    cur.execute("DELETE FROM ag.ag_kit_barcodes "
                                "WHERE ag_kit_id IN %s",
                                (tuple(ag_kit_ids),))

                    cur.execute("DELETE FROM ag.ag_kit "
                                "WHERE ag_kit_id IN %s",
                                (tuple(ag_kit_ids),))

                # Delete barcodes and project-barcode associations
                cur.execute("SELECT barcode "
                            "FROM barcodes.barcode "
                            "WHERE kit_id=%s",
                            (curr_kit_id,))
                barcodes_fetch = cur.fetchall()

                if len(barcodes_fetch) > 0:
                    barcodes = barcodes_fetch[0]
                    cur.execute("DELETE FROM barcodes.project_barcode "
                                "WHERE barcode IN %s",
                                (tuple(barcodes),))

                    cur.execute("DELETE FROM barcodes.barcode "
                                "WHERE barcode IN %s",
                                (tuple(barcodes),))

                # Delete the kit itself
                cur.execute("DELETE FROM barcodes.kit "
                            "WHERE kit_id=%s",
                            (curr_kit_id,))

    @staticmethod
    def _delete_kits_and_dak_orders_to_kits(kit_ids):
        with Transaction() as t:
            DaklapackPollingTests._delete_dak_orders_to_kits(t, kit_ids)
            DaklapackPollingTests._delete_kits(t, kit_ids)
            t.commit()

    def _check_last_polling_status(self, dak_order_id, expected_status):
        with Transaction() as t:
            with t.dict_cursor() as cur:
                cur.execute("SELECT last_polling_status "
                            "FROM barcodes.daklapack_order "
                            "WHERE dak_order_id =  %s",
                            (dak_order_id,))
                curr_records = cur.fetchall()
                self.assertEqual(len(curr_records), 1)
                self.assertEqual(expected_status, curr_records[0][0])

    def test_poll_dak_orders(self):
        order_statuses_pg_1 = {
            "isSuccess": True,
            "messages": None,
            "total": 3,
            "data": [
                {
                    "id": "020a5c97-6837-4bc2-99e6-7cdad38230e7",
                    "orderId": "abc917ef-0c4d-431a-9aa0-0a1f4f41f44b",
                    "creationDate": "2021-02-26T08:30:18.805519Z",
                    "plannedSendDate": None,
                    "statusLedger": [
                        {
                            "changeDate": "2021-02-26T08:30:18.8050976Z",
                            "status": "New",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T09:30:18.8050976Z",
                            "status": "Inproduction",
                            "origin": "OrderApi",
                            "description": ""
                        }
                    ],
                    "lastState": {
                        "changeDate": "2021-02-26T08:41:43.0786247Z",
                        "status": "Inproduction",
                        "origin": "OrderApi",
                        "description": ""
                    },
                    "shippingProvider": {
                        "name": "FedEx",
                        "shippingType": "FEDEX_2_DAY"
                    },
                    "orderLines": [
                        {
                            "articleId": "350100",
                            "amount": 2
                        }
                    ],
                    "code": None,
                    "reference": None,
                    "nawId": "20b34834-3399-4cfd-9abe-accdbf34e3e2"
                },
                {
                    "id": "4b96304d-96ff-4ab3-8eb6-0aa44046d69b",
                    "orderId": "0ed917ef-0c4d-431a-9aa0-0a1f4f41f44b",
                    "creationDate": "2021-02-26T08:36:00.2250124Z",
                    "plannedSendDate": None,
                    "statusLedger": [
                        {
                            "changeDate": "2021-02-26T08:36:00.2245913Z",
                            "status": "New",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T09:30:18.8050976Z",
                            "status": "Inproduction",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T08:49:28.2010144Z",
                            "status": "Sent",
                            "origin": "OrderApi",
                            "description": ""
                        }
                    ],
                    "lastState": {
                        "changeDate": "2021-02-26T08:49:28.2010144Z",
                        "status": "Sent",
                        "origin": "OrderApi",
                        "description": ""
                    },
                    "shippingProvider": {
                        "name": "FedEx",
                        "shippingType": "FEDEX_2_DAY"
                    },
                    "orderLines": [
                        {
                            "articleId": "350100",
                            "amount": 2
                        }
                    ],
                    "code": None,
                    "reference": None,
                    "nawId": "a236b632-b77a-4f3b-b537-75e58c9fae77"
                }
            ]
        }

        order_statuses_pg_2 = {
            "isSuccess": True,
            "messages": None,
            "total": 3,
            "data": [
                {
                    # This one won't be in our db's list of open orders;
                    # we're imagining it was seen/dealt with in the past
                    "id": "566bdadb-df00-462b-9bfc-1f1c652216ed",
                    "orderId": "OX3HOOD",
                    "creationDate": "2021-02-26T08:36:12.4267351Z",
                    "plannedSendDate": None,
                    "statusLedger": [
                        {
                            "changeDate": "2021-02-26T08:36:12.4263206Z",
                            "status": "New",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T09:30:18.8050976Z",
                            "status": "Inproduction",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T08:41:43.0786247Z",
                            "status": "Error",
                            "origin": "OrderApi",
                            "description": ""
                        }
                    ],
                    "lastState": {
                        "changeDate": "2021-02-26T08:41:43.0786247Z",
                        "status": "Error",
                        "origin": "OrderApi",
                        "description": ""
                    },
                    "shippingProvider": {
                        "name": "FedEx",
                        "shippingType": "FEDEX_2_DAY"
                    },
                    "orderLines": [
                        {
                            "articleId": "350100",
                            "amount": 2
                        }
                    ],
                    "code": None,
                    "reference": None,
                    "nawId": "84169469-4e84-4b73-833b-1b790baebc20"
                },
                {
                    "id": "AACbdadb-df00-462b-9bfc-1f1c652216ed",
                    "orderId": "8ed917ef-0c4d-431a-9aa0-0a1f4f41f44b",
                    "creationDate": "2021-02-26T08:36:12.4267351Z",
                    "plannedSendDate": None,
                    "statusLedger": [
                        {
                            "changeDate": "2021-02-26T08:36:12.4263206Z",
                            "status": "New",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T09:30:18.8050976Z",
                            "status": "Inproduction",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T08:41:43.0786247Z",
                            "status": "Error",
                            "origin": "OrderApi",
                            "description": ""
                        }
                    ],
                    "lastState": {
                        "changeDate": "2021-02-26T08:41:43.0786247Z",
                        "status": "Error",
                        "origin": "OrderApi",
                        "description": ""
                    },
                    "shippingProvider": {
                        "name": "FedEx",
                        "shippingType": "FEDEX_2_DAY"
                    },
                    "orderLines": [
                        {
                            "articleId": "350100",
                            "amount": 2
                        }
                    ],
                    "code": None,
                    "reference": None,
                    "nawId": "84169469-4e84-4b73-833b-1b790baebc20"
                },
                {
                    "id": "DDCbdadb-df00-462b-9bfc-1f1c652216ed",
                    "orderId": "bf3ef5f7-ae20-45d0-8cfb-d5c0db8024fe",
                    "creationDate": "2021-02-26T08:36:12.4267351Z",
                    "plannedSendDate": None,
                    "statusLedger": [
                        {
                            "changeDate": "2021-02-26T08:36:12.4263206Z",
                            "status": "New",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T09:30:18.8050976Z",
                            "status": "Inproduction",
                            "origin": "OrderApi",
                            "description": ""
                        },
                        {
                            "changeDate": "2021-02-26T08:41:43.0786247Z",
                            "status": "Sent",
                            "origin": "OrderApi",
                            "description": ""
                        }
                    ],
                    "lastState": {
                        "changeDate": "2021-02-26T08:41:43.0786247Z",
                        "status": "Sent",
                        "origin": "OrderApi",
                        "description": ""
                    },
                    "shippingProvider": {
                        "name": "FedEx",
                        "shippingType": "FEDEX_2_DAY"
                    },
                    "orderLines": [
                        {
                            "articleId": "350100",
                            "amount": 2
                        }
                    ],
                    "code": None,
                    "reference": None,
                    "nawId": "84169469-4e84-4b73-833b-1b790baebc20"
                }
            ]
        }

        order_statuses_pg_3 = {
            "isSuccess": True,
            "messages": None,
            "total": 3,
            "data": []
        }

        registration_card_ids = ["DEFR", "DEFR2"]
        articles_for_orders = [
            {"articles": [
                {"articleCode": "350100",
                 "total": 1,
                 "new": 0,
                 "inProduction": 0,
                 "sent": 1,
                 "errors": 0,
                 "articles": [
                     {"internalId": "8abf7149-4889-42b3-8368-1b68284d5b95",
                      "articleCode": "350100",
                      "status": "Sent",
                      "description": None,
                      "sendInformation": {
                          "firstName": "Natalia J Phillips", "lastName": "",
                          "address1": "2166  Chapmans Lane", "insertion": "",
                          "address2": "", "postalCode": "88103",
                          "city": "Clovis",
                          "state": "NM", "country": "USA", "countryCode": "US",
                          "phone": "505-784-5252", "companyName": "Jane Doe"
                      },
                      "shippingProvider": {
                          "name": "FedEx", "shippingType": "FEDEX_2_DAY"
                      },
                      "scannableKitItems": [
                          {"type": "KitId", "barcode": "DEFR",
                           "creationDate": "2021-02-26T08:48:16.788439Z",
                           "itemCount": 1,
                           "containerItems": []
                           },
                          {"type": "Tube", "barcode": "DEFT",
                           "creationDate": "2021-02-26T08:48:16.7885478Z",
                           "itemCount": 1,
                           "containerItems": []
                           },
                          {"type": "BoxId", "barcode": "DEFX",
                           "creationDate": "2021-02-26T08:48:16.788439Z",
                           "itemCount": 1,
                           "containerItems": []
                           }
                      ],
                      "inBoundDelivery": None,
                      "outBoundDelivery": None,
                      "code": None, "plannedSendDate": None
                      }  # end article instance
                 ]}
                # end "articles" (instance) list, single article (type) entry
            ]},  # end "articles" (type) list, outer dict
            {"articles": [
                {"articleCode": "350102",
                 "total": 1,
                 "new": 0,
                 "inProduction": 0,
                 "sent": 1,
                 "errors": 0,
                 "articles": [
                     {"internalId": "8abf7149-4889-42b3-8368-1b68284d5b95",
                      "articleCode": "350100",
                      "status": "Sent",
                      "description": None,
                      "sendInformation": {
                          "firstName": "John J Doe", "lastName": "",
                          "address1": "1  East Lane", "insertion": "",
                          "address2": "", "postalCode": "88103",
                          "city": "Truth or Consequences",
                          "state": "NM", "country": "USA", "countryCode": "US",
                          "phone": "505-784-5252", "companyName": "Jane Doe"
                      },
                      "shippingProvider": {
                          "name": "FedEx", "shippingType": "FEDEX_2_DAY"
                      },
                      "scannableKitItems": [
                          {"type": "KitId", "barcode": "DEFR2",
                           "creationDate": "2021-02-26T08:48:16.788439Z",
                           "itemCount": 1,
                           "containerItems": []
                           },
                          {"type": "Tube", "barcode": "DEFT2",
                           "creationDate": "2021-02-26T08:48:16.7885478Z",
                           "itemCount": 1,
                           "containerItems": []
                           },
                          {"type": "BoxId", "barcode": "DEFX2",
                           "creationDate": "2021-02-26T08:48:16.788439Z",
                           "itemCount": 1,
                           "containerItems": []
                           }
                      ],
                      "inBoundDelivery": None,
                      "outBoundDelivery": None,
                      "code": None, "plannedSendDate": None
                      }  # end article instance
                 ]}
                # end "articles" (instance) list, single article (type) entry
            ]}  # end "articles" (type) list, outer dict
        ]

        expected_out = {
            'Error':
                [{'article_code': '350100',
                  'creation_date': '2021-02-26T08:36:12.4267351Z',
                  'order_id': '8ed917ef-0c4d-431a-9aa0-0a1f4f41f44b',
                  'order_submitter': 'Jane Doe',
                  'sent_to_address': {
                      'address1': '1  East Lane',
                      'address2': '',
                      'city': 'Truth or Consequences',
                      'companyName': 'Jane Doe',
                      'country': 'USA',
                      'countryCode': 'US',
                      'firstName': 'John J Doe',
                      'insertion': '',
                      'lastName': '',
                      'phone': '505-784-5252',
                      'postalCode': '88103',
                      'state': 'NM'},
                  'status_description': None}],
            'Sent':
                [{'created': [
                    {'address': {'firstName': 'Natalia J Phillips',
                                 'lastName': '',
                                 'address1': '2166  Chapmans Lane',
                                 'insertion': '',
                                 'address2': '', 'postalCode': '88103',
                                 'city': 'Clovis', 'state': 'NM',
                                 'country': 'USA', 'countryCode': 'US',
                                 'phone': '505-784-5252',
                                 'companyName': 'Jane Doe'},
                     'box_id': 'DEFX',
                     'inbound_fedex_tracking': None,
                     'kit_id': 'DEFR',
                     'outbound_fedex_tracking': None,
                     'sample_barcodes': ['DEFT']}]}],
            'Code Error':
                ["<class 'StopIteration'>: "]}

        # clean up any lingering test records before beginning
        self._delete_kits_and_dak_orders_to_kits(registration_card_ids)

        try:
            with Transaction() as t:
                self.make_dummy_dak_orders(t, bonus_records=True)
                t.commit()

            # NB: these have to be patched *where they will be looked up*,
            # not where they are originally defined; see
            # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
            with patch("microsetta_private_api.admin."
                       "daklapack_communication.get_daklapack_orders_"
                       "status") as mock_dak_orders_info:
                mock_dak_orders_info.side_effect = [make_test_response(
                    200, order_statuses_pg_1), make_test_response(
                    200, order_statuses_pg_2), make_test_response(
                    200, order_statuses_pg_3)]

                with patch(
                        "microsetta_private_api.admin.daklapack_communication."
                        "get_daklapack_order_details") as mock_dak_order_info:
                    mock_dak_order_info.side_effect = [make_test_response(
                        200, articles_for_orders[0]), make_test_response(
                        200, articles_for_orders[1])]

                    with patch("microsetta_private_api.admin."
                               "daklapack_communication."
                               "post_daklapack_order_archive") as mock_archive:
                        mock_archive.side_effect = [make_test_response(
                            200, {"updated": 1})]

                        with patch("microsetta_private_api.admin."
                                   "daklapack_communication.send_"
                                   "daklapack_order_errors_report_email") as \
                                mock_order_email:
                            mock_order_email.side_effect = [True]

                            with patch("microsetta_private_api.admin."
                                       "daklapack_communication.send_daklapack"
                                       "_polling_errors_report_email") as \
                                    mock_polling_email:
                                mock_polling_email.side_effect = [True]

                                real_out = poll_dak_orders()

            # for three incomplete orders that saved, check status in db
            self._check_last_polling_status(
                "abc917ef-0c4d-431a-9aa0-0a1f4f41f44b", "Inproduction")
            self._check_last_polling_status(
                "0ed917ef-0c4d-431a-9aa0-0a1f4f41f44b", "Sent")
            # this order had a status of "Error" in the daklapack response but
            # this is changed to "Archived" after we archive the errored order
            self._check_last_polling_status(
                "8ed917ef-0c4d-431a-9aa0-0a1f4f41f44b", "Archived")
            # this order is open in our db but dak api gives no info on it
            self._check_last_polling_status(
                "99746684-8a2b-45d9-9337-4742bf6734cc", None)

            # remove the kit_uuid from the real output before testing
            # since that can't be known ahead of time
            del real_out["Sent"][0]["created"][0]["kit_uuid"]
            self.assertEqual(expected_out, real_out)
        finally:
            self._delete_kits_and_dak_orders_to_kits(registration_card_ids)

    def test_process_order_articles_sent_status(self):
        expected_out = [
            {'created': [
                {'kit_id': 'ABCR',
                 'address': {'firstName': 'Natalia J Phillips',
                             'lastName': '',
                             'address1': '2166  Chapmans Lane',
                             'insertion': '',
                             'address2': '', 'postalCode': '88103',
                             'city': 'Clovis', 'state': 'NM',
                             'country': 'USA', 'countryCode': 'US',
                             'phone': '505-784-5252',
                             'companyName': 'Jane Doe'},
                 'box_id': 'ABCX',
                 'outbound_fedex_tracking': 'Tracking Code 1',
                 'inbound_fedex_tracking': 'Tracking Code 2',
                 'sample_barcodes': ['ABCT', 'ABCN']
                 },
            ]},
            {'created': [
                {'kit_id': 'ABCR2',
                 'box_id': 'ABCX2',
                 'address': {'firstName': 'Natalia J Phillips',
                             'lastName': '',
                             'address1': '2166  Chapmans Lane',
                             'insertion': '',
                             'address2': '', 'postalCode': '88103',
                             'city': 'Clovis', 'state': 'NM',
                             'country': 'USA', 'countryCode': 'US',
                             'phone': '505-784-5252',
                             'companyName': 'Jane Doe'},
                 'outbound_fedex_tracking': 'Tracking Code 2',
                 'inbound_fedex_tracking': None,
                 'sample_barcodes': ['ABCT2', 'ABCN2']
                 }
            ]},
            {'created': [
                {'kit_id': 'DEFR',
                 'box_id': 'DEFX',
                 'address': {'firstName': 'Natalia J Phillips',
                             'lastName': '',
                             'address1': '2166  Chapmans Lane',
                             'insertion': '',
                             'address2': '', 'postalCode': '88103',
                             'city': 'Clovis', 'state': 'NM',
                             'country': 'USA', 'countryCode': 'US',
                             'phone': '505-784-5252',
                             'companyName': 'Jane Doe'},
                 'outbound_fedex_tracking': None,
                 'inbound_fedex_tracking': None,
                 'sample_barcodes': ['DEFT']
                 }
            ]}
        ]

        with Transaction() as t:
            dummy_orders = self.make_dummy_dak_orders(t)
            an_order_id = dummy_orders[0][0]
            admin_repo = AdminRepo(t)

            # NB: these have to be patched *where they will be looked up*, not
            # where they are originally defined; see
            # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
            with patch("microsetta_private_api.admin.daklapack_communication."
                       "get_daklapack_order_details") as mock_dak_order_info:
                mock_dak_order_info.side_effect = [make_test_response(
                    200, self.ARTICLES_INFO)]

                real_out = process_order_articles(
                    admin_repo, an_order_id, "Sent",
                    "2021-02-26T08:30:18.805519Z")

                self.assertEqual(len(expected_out), len(real_out))
                # kit uuids can't be predicted for test, so pop them out
                for curr_created_dict in real_out:
                    curr_details_dict = curr_created_dict["created"][0]
                    curr_details_dict.pop("kit_uuid")
                self.assertEqual(expected_out, real_out)

        # Note: transaction is not committed so db changes don't stick :)

    def test_process_order_articles_error_status(self):
        expected_out = [
            {'article_code': '350201',
             'creation_date': '2021-02-26T08:30:18.805519Z',
             'order_id': '7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b',
             'order_submitter': 'Jane Doe',
             'sent_to_address': {
                 'address1': '2166  Chapmans Lane',
                 'address2': '',
                 'city': 'Clovis',
                 'companyName': 'Jane Doe',
                 'country': 'USA',
                 'countryCode': 'US',
                 'firstName': 'Natalia J Phillips',
                 'insertion': '',
                 'lastName': '',
                 'phone': '505-784-5252',
                 'postalCode': '88103',
                 'state': 'NM'},
             'status_description': "A test description"},
            {'article_code': '350201',
             'creation_date': '2021-02-26T08:30:18.805519Z',
             'order_id': '7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b',
             'order_submitter': 'Jane Doe',
             'sent_to_address':
                 {'address1': '2166  Chapmans Lane',
                  'address2': '',
                  'city': 'Clovis',
                  'companyName': 'Jane Doe',
                  'country': 'USA',
                  'countryCode': 'US',
                  'firstName': 'Natalia J Phillips',
                  'insertion': '',
                  'lastName': '',
                  'phone': '505-784-5252',
                  'postalCode': '88103',
                  'state': 'NM'},
             'status_description': None},
            {'article_code': '350100',
             'creation_date': '2021-02-26T08:30:18.805519Z',
             'order_id': '7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b',
             'order_submitter': 'Jane Doe',
             'sent_to_address': {
                 'address1': '2166  Chapmans Lane',
                 'address2': '',
                 'city': 'Clovis',
                 'companyName': 'Jane Doe',
                 'country': 'USA',
                 'countryCode': 'US',
                 'firstName': 'Natalia J Phillips',
                 'insertion': '',
                 'lastName': '',
                 'phone': '505-784-5252',
                 'postalCode': '88103',
                 'state': 'NM'},
             'status_description': None}]

        with Transaction() as t:
            dummy_orders = self.make_dummy_dak_orders(t)
            an_order_id = dummy_orders[0][0]
            admin_repo = AdminRepo(t)

            # NB: these have to be patched *where they will be looked up*, not
            # where they are originally defined; see
            # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
            with patch("microsetta_private_api.admin.daklapack_communication."
                       "get_daklapack_order_details") as mock_dak_order_info:
                # NB: this is returning the same json as for the "sent"
                # case; this json says each article was sent (which would
                # not be the case in the "error" case) but that field isn't
                # used for the "error" case so I am not bothering to make a
                # whole new input to change that field for verisimilitude
                mock_dak_order_info.side_effect = [make_test_response(
                    200, self.ARTICLES_INFO)]

                real_out = process_order_articles(
                    admin_repo, an_order_id, "Error",
                    "2021-02-26T08:30:18.805519Z")

                self.assertEqual(len(expected_out), len(real_out))
                # # kit uuids can't be predicted for test, so pop them out
                # for curr_created_dict in real_out:
                #     curr_details_dict = curr_created_dict["created"][0]
                #     curr_details_dict.pop("kit_uuid")
                self.assertEqual(expected_out, real_out)

        # Note: transaction is not committed so db changes don't stick :)

    def test_process_order_articles_unknown_status(self):
        with Transaction() as t:
            dummy_orders = self.make_dummy_dak_orders(t)
            an_order_id = dummy_orders[0][0]
            admin_repo = AdminRepo(t)

            # NB: these have to be patched *where they will be looked up*, not
            # where they are originally defined; see
            # https://docs.python.org/3/library/unittest.mock.html#where-to-patch
            with patch("microsetta_private_api.admin.daklapack_communication."
                       "get_daklapack_order_details") as mock_dak_order_info:
                # NB: this is returning the same json as for the "sent"
                # case; this json says each article was sent (which would
                # not be the case in the "unknown" case) but that field isn't
                # used for the "unknown" case so I am not bothering to make a
                # whole new input to change that field for verisimilitude
                mock_dak_order_info.side_effect = [make_test_response(
                    200, self.ARTICLES_INFO)]

                with self.assertRaisesRegex(
                        ValueError,
                        "Order 7ed917ef-0c4d-431a-9aa0-0a1f4f41f44b "
                        "has an unexpected status: InProduction"):
                    process_order_articles(
                        admin_repo, an_order_id, "InProduction",
                        "2021-02-26T08:30:18.805519Z")

        # Note: transaction is not committed so db changes don't stick :)
