# shasta/shasta.py
# TODO: use _get or _list when getting a list?
# TODO: Covert request answer to object
from .vars import *
from .helper import Caller


class Shasta:
    def __init__(self, ckey_, key_=None, env='sandbox'):
        self.key_ = key_
        self.ckey_ = ckey_
        enp = SANDBOX
        if env == 'live':
            enp = LIVE
        self.r = Caller(enp, {'Authorization': 'Bearer {}'.format(self.ckey_)})

    # Object: Project
    def project_get(self):
        return self.r.get('/project')

    def project_edit(self, project):
        return self.r.patch('/project', project)

    # Object: Account
    def accounts_get(self, limit=10, cursor=None):
        return self.r.get('/accounts?limit={}&cursor={}'.format(limit, cursor))

    def account_create(self, account):
        return self.r.post('/accounts', account.send())

    def account_get(self, account_id):
        return self.r.get('/accounts/' + str(account_id))

    def account_edit(self, account_id, account):
        return self.r.patch('/accounts/{}'.format(account_id), account.patch())

    # Object: Transaction
    def transactions_get(self, limit=10, cursor=None):
        return self.r.get('/transactions?limit={}&cursor={}'.format(limit, cursor))

    def account_transactions_get(self, account_id, limit=10, cursor=None):
        return self.r.get('/accounts/{}/transactions?limit={}&cursor={}'.format(account_id, limit, cursor))

    def transaction_get(self, transaction_id):
        return self.r.get('/transactions/{}'.format(transaction_id))

    # Object: Customer
    def customers_get(self, limit=10, cursor=None):
        return self.r.get('/customers?limit={}&cursor={}'.format(limit, cursor))

    def customer_create(self, customer):
        return self.r.post('/customers', customer.send())

    def customer_get(self, customer_id):
        return self.r.get('/customers/{}'.format(customer_id))

    def customer_edit(self, customer_id, customer):
        return self.r.patch('/customers/{}'.format(customer_id), customer.patch())

    # Object: Transfer
    def transfers_get(self, limit=10, cursor=None):
        return self.r.get('/transfers?limit={}&cursor={}'.format(limit, cursor))

    def transfer_create(self, transfer):
        return self.r.post('/transfers', transfer.send())

    def transfer_get(self, transfer_id):
        return self.r.get('/transfers/{}'.format(transfer_id))

    def transfer_edit(self, transfer_id, transfer):
        return self.r.patch('/transfers/{}'.format(transfer_id), transfer.patch())

    # Object: CardInfo
    def card_token_create(self, card_info):
        return self.r.post('/acquiring/card_tokens', card_info.send())

    def card_token_get(self, card_token_id):
        return self.r.get('/acquiring/card_tokens/{}'.format(card_token_id))

    # Object: Card
    def cards_get(self, limit=10, cursor=None):
        return self.r.get('/acquiring/cards?limit={}&cursor={}'.format(limit, cursor))

    def card_create(self, card):
        return self.r.post('/acquiring/cards', card.send())

    def card_get(self, card_id):
        return self.r.get('/acquiring/cards/{}'.format(card_id))

    def card_edit(self, card_id, card):
        return self.r.patch('/acquiring/cards/{}'.format(card_id), card.patch())

    # Object: CardPayins
    def card_payins_get(self, limit=10, cursor=None):
        return self.r.get('/acquiring/card_payins?limit={}&cursor={}'.format(limit, cursor))

    def card_payin_create(self, card_payin):
        return self.r.post('/acquiring/card_payins', card_payin.send())

    def card_payin_get(self, card_payin_id):
        return self.r.get('/acquiring/card_payins/{}'.format(card_payin_id))

    def card_payin_edit(self, card_payin_id, card_payin):
        return self.r.patch('/acquiring/card_payins/{}'.format(card_payin_id), card_payin.patch())

    def card_payin_finish(self, card_payin_id):
        self.r.post('/acquiring/card_payins/{}/finish'.format(card_payin_id))

    def card_payin_refunds_get(self, limit=10, cursor=None):
        return self.r.get('/acquiring/card_payin_refunds?limit={}&cursor={}'.format(limit, cursor))

    def card_payin_refund_create(self, card_payin_refund):
        return self.r.post('/acquiring/card_payin_refunds', card_payin_refund)

    def card_payin_refund_get(self, card_payin_refund_id):
        return self.r.get('/acquiring/card_payin_refunds/{}'.format(card_payin_refund_id))

    def card_payin_refund_edit(self, card_payin_refund_id, card_payin_refund):
        return self.r.patch('/acquiring/card_payin_refunds/{}'.format(card_payin_refund_id), card_payin_refund)

    # Object: CardVerification
    def card_verifications_get(self, limit=10, cursor=None):
        return self.r.get('/acquiring/card_verifications?limit={}&cursor={}'.format(limit, cursor))

    def card_verification_create(self, card_verification):
        return self.r.post('/acquiring/card_verifications', card_verification.send())

    def card_verification_get(self, card_verification_id):
        return self.r.get('/acquiring/card_verifications/{}'.format(card_verification_id))

    def card_verification_edit(self, card_verification_id, card_verification):
        return self.r.patch('/acquiring/card_verifications/{}'.format(card_verification_id), card_verification_id.patch())

    def card_verification_finish(self, card_verification_id):
        return self.r.post('/acquiring/card_verifications/{}/finish'.format(card_verification_id))

    # Object: BankAccount
    def bank_accounts_get(self, limit=10, cursor=None):
        return self.r.get('/bank_accounts?limit={}&cursor={}'.format(limit, cursor))

    def bank_account_create(self, bank_account):
        return self.r.post('/bank_accounts', bank_account.send())

    def bank_account_get(self, bank_account_id):
        return self.r.get('/bank_accounts/{}'.format(bank_account_id))

    def bank_account_edit(self, bank_account_id, bank_account):
        return self.r.patch('/bank_accounts/{}'.format(bank_account_id), bank_account.patch())

    # Object: BankPayinReferences
    def bank_payin_references_get(self, limit=10, cursor=None):
        # TODO: Use .get_list for lists?
        return self.r.get_list('/bank_payin_references', limit, cursor)

    def bank_payin_reference_create(self, bank_payin_method):
        return self.r.post('/bank_payin_references', bank_payin_method.send())

    def bank_payin_reference_get(self, bank_payin_reference_id):
        return self.r.get('/bank_payin_references/{}'.format(bank_payin_reference_id))

    def bank_payin_reference_edit(self, bank_payin_reference_id, bank_payin_reference):
        return self.r.patch('/bank_payin_references/{}'.format(bank_payin_reference_id), bank_payin_reference.patch())

    # Object: BankPayin
    def bank_payins_get(self, limit=10, cursor=None):
        return self.r.get_list('/bank_payins', limit, cursor)

    def bank_payin_get(self, bank_payin_id):
        return self.r.get('/bank_payins/{}'.format(bank_payin_id))

    def bank_payin_edit(self, bank_payin_id, bank_payin):
        return self.r.patch('/bank_payins/{}'.format(bank_payin_id), bank_payin.patch())

    # Object: BankPayout
    def bank_payouts_get(self, limit=10, cursor=None):
        return self.r.get_list('/bank_payouts', limit, cursor)

    def bank_payout_create(self, bank_payout):
        return self.r.post('/bank_payouts', bank_payout)

    def bank_payout_get(self, bank_payout_id):
        return self.r.get('/bank_payouts/{}'.format(bank_payout_id))

    def bank_payout_edit(self, bank_payout_id, bank_payout):
        return self.r.patch('/bank_payouts/{}'.format(bank_payout_id), bank_payout.patch())

    # Object: File
    def files_get(self, limit=10, cursor=None):
        return self.r.get_list('/files', limit, cursor)

    def file_upload(self, file):
        return self.r.post('/files', file.send())

    def file_get(self, file_id):
        return self.r.get('/files/{}'.format(file_id))

    def file_delete(self, file_id):
        return self.r.delete('/files/{}'.format(file_id))

    def file_download(self, file_id):
        return self.r.get('/files/{}/download'.format(file_id))

    # Object: Webhooks
    def webhooks_get(self, limit=10, cursor=None):
        return self.r.get_list('/webhooks', limit, cursor)

    def webhook_create(self, webhook):
        return self.r.post('/webhooks', webhook.send())

    def webhook_get(self, webhook_id):
        return self.r.get('/webhooks/{}'.format(webhook_id))

    def webhook_delete(self, webhook_id):
        return self.r.delete('/webhooks/{}'.format(webhook_id))

    def webhook_edit(self, webhook_id, webhook):
        return self.r.patch('/webhooks/{}'.format(webhook_id), webhook.patch())

    # Object: Invoice
    def invoices_get(self, limit=10, cursor=None):
        return self.r.get_list('/invoices', limit, cursor)

    def invoice_get(self, invoice_id):
        return self.r.get('/invoices/{}'.format(invoice_id))

    # Object: FakeData
    def fake_data(self):
        return self.r.post('/fake_data')





