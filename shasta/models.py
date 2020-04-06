# shasta/models.py
# TODO: Add all classes and all attributes


class Project:
    def __init(self, project_id, created_at, default_card_payin_instant_account_ids, default_card_payin_fee_account_ids,
               card_payin_fee, card_payin_fee_non_eu, vendor, meta):
        """
        :param project_id: string
        :param created_at: string
        :param default_card_payin_instant_account_ids: map (AccountID)
        :param default_card_payin_fee_account_ids: map (AccountID)
        :param card_payin_fee: string
        :param card_payin_fee_non_eu: string
        :param vendor: Vendor
        :param meta: Meta
        """
        self.project_id = project_id
        self.created_at = created_at
        self.default_card_payin_instant_account_ids = default_card_payin_instant_account_ids
        self.default_card_payin_fee_account_ids = default_card_payin_fee_account_ids
        self.card_payin_fee = card_payin_fee
        self.card_payin_fee_non_eu = card_payin_fee_non_eu
        self.vendor = vendor
        self.meta = meta

    def patch(self):
        return {
            'default_card_payin_instant_account_id': self.default_card_payin_instant_account_id,
            'meta': self.meta
        }


class Account:
    def __init__(self, currency, allow_negative_balance=None, customer_id=None, auto_bank_payout=None, meta=None):
        """
        :param currency:
        :param allow_negative_balance: boolean
        :param customer_id:
        :param auto_bank_payout: AutoBankPayout
        :param meta: Meta
        """
        self.currency = currency
        self.allow_negative_balance = allow_negative_balance
        self.customer_id = customer_id
        self.auto_bank_payout = auto_bank_payout
        self.meta = meta

    def send(self):
        # TODO: Figure out --> auto_bank_payout
        # TODO: Check the meta param
        data = {
            'currency': self.currency
        }
        if self.allow_negative_balance:
            data['allow_negative_balance'] = self.allow_negative_balance
        if self.customer_id:
            data['customer_id'] = self.customer_id
        if self.auto_bank_payout:
            data['auto_bank_payout'] = self.auto_bank_payout
        if self.meta:
            data['meta'] = self.meta
        return data

    def patch(self):
        return {
            'allow_negative_balance': self.allow_negative_balance,
            'meta': self.meta
        }


class Customer:
    def __init__(self, first_name=None, last_name=None, email_address=None, phone_number=None, nationality=None,
                 employment_status=None, address=None, document=None, meta=None):
        """
        :param first_name: string
        :param last_name: string
        :param email_address: string
        :param phone_number: string
        :param nationality: string
        :param employment_status: string enum: [student, employed, self_employed, searching, not_employed]
        :param address: Address
        :param document: Document
        :param meta: Meta
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.nationality = nationality
        self.employment_status = employment_status
        self.address = address
        self.document = document
        self.meta = meta

    def send(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email_address': self.email_address,
            'phone_number': self.phone_number,
            'nationality': self.nationality,
            'employment_status': self.employment_status,
            'address': self.address.send(),
            'document': self.document.send(),
            'meta': self.meta
        }

    def patch(self):
        return self.send()


class Address:
    def __init__(self, line_1, line_2, postal_code, city, region, country):
        """
        :param line_1: string
        :param line_2: string
        :param postal_code: string
        :param city: string
        :param region: string
        :param country: string
        """
        self.line_1 = line_1
        self.line_2 = line_2
        self.postal_code = postal_code
        self.city = city
        self.region = region
        self.country = country

    def send(self):
        return {
            'line_1': self.line_1,
            'line_2': self.line_2,
            'postal_code': self.postal_code,
            'city': self.city,
            'region': self.region,
            'country': self.country,
        }


class Document:
    def __init__(self, type, country, number, expiration_date, front_file_id, back_file_id, selfie_file_id,
                 verification_file_id):
        """
        :param type: string emun: [national_id, passport, driving_license]
        :param country: string
        :param number: string
        :param expiration_date: date
        :param front_file_id: string
        :param back_file_id: string
        :param selfie_file_id: string
        :param verification_file_id: string
        """
        self.type = type
        self.country = country
        self.number = number
        self.expiration_date = expiration_date
        self.front_file_id = front_file_id
        self.back_file_id = back_file_id
        self.selfie_file_id = selfie_file_id
        self.verification_file_id = verification_file_id

    def send(self):
        data = {
            'type': self.type,
            'country': self.country,
            'number': self.number,
            'expiration_date': self.expiration_date,
            'front_file_id': self.front_file_id,
            'back_file_id': self.back_file_id,
            'selfie_file_id': self.selfie_file_id,
            'verification_file_id': self.verification_file_id
        }


class Transfer:
    def __init__(self, source_account_id=None, destination_account_id=None, value=None, meta=None):
        """
        :param source_account_id: string (AccountID)
        :param destination_account_id: string (AccountID)
        :param value: Value
        :param meta: Meta
        """
        self.source_account_id = source_account_id
        self.destination_account_id = destination_account_id
        self.value = value
        self.meta = self.meta

    def send(self):
        return {
            'source_account_id': self.source_account_id,
            'destination_account_id': self.destination_account_id,
            'value': self.value,
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class CardInfo:
    def __init__(self, number, expiration_month, expiration_year, cvv, brand=None, country=None, bank_name=None,
                 is_sepa=None, type=None, prepaid=None):
        """

        :param number: string (card) - Card number without spaces
        :param expiration_month: integer - Expiration month (1-12)
        :param expiration_year: integer - Full expiration year
        :param cvv: string - CVC/CVV
        :param brand: string
        :param country: string (country)
        :param bank_name: string
        :param is_sepa: boolean
        :param type: string
        :param prepaid: boolean
        """
        self.number = number
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.cvv = cvv
        self.brand = brand
        self.country = country
        self.bank_name = bank_name
        self.is_sepa = is_sepa
        self.type = type
        self.prepaid = prepaid

    def send(self):
        data = {
            'number': self.number,
            'expiration_month': self.expiration_month,
            'expiration_year': self.expiration_year,
            'cvv': self.cvv
        }
        if self.brand:
            data['brand'] = self.brand
        if self.country:
            data['country'] = self.country
        if self.bank_name:
            data['bank_name'] = self.bank_name
        if self.is_sepa:
            data['is_sepa'] = self.is_sepa
        if self.type:
            data['type'] = self.type
        if self.prepaid:
            data['prepaid'] = self.prepaid
        return data


class Card:
    def __init__(self, customer_id, card_token_id, card_info, meta):
        """
        :param customer_id: string (CustomerID) default: null
        :param card_token_id: string (CardTokenID)
        :param card_info: CardInfo
        :param meta: Meta
        """
        self.customer_id = customer_id
        self.card_token_id = card_token_id
        self.card_info = card_info
        self.meta = meta

    def send(self):
        return {
            'customer_id': self.customer_id,
            'card_token_id': self.card_token_id,
            'card_info': self.card_info.send(),
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class CardPayin:
    def __init__(self, account_id, value, card_info, card_token_id, card_id, is_secure, secure_redirect_url, is_instant,
                 instant_account_id, fee_account_id, meta=None):
        """
        :param account_id: string (AccountID)
        :param value: Value
        :param card_info: CardInfo
        :param card_token_id: string (CardTokenID)
        :param card_id: string (CardID)
        :param is_secure: boolean
        :param secure_redirect_url: string
        :param is_instant: boolean
        :param instant_account_id: string (AccountID)
        :param fee_account_id: string (AccountID)
        :param meta: Meta
        """
        self.account_id = account_id
        self.value = value
        self.card_info = card_info
        self.card_token_id = card_token_id
        self.card_id = card_id
        self.is_secure = is_secure
        self.secure_redirect_url = secure_redirect_url
        self.is_instant = is_instant
        self.instant_account_id = instant_account_id
        self.fee_account_id = fee_account_id
        self.meta = meta

    def send(self):
        return {
            'account_id': self.account_id,
            'value': self.value.send(),
            'card_info': self.card_info.send(),
            'card_token_id': self.card_token_id,
            'card_id': self.card_id,
            'is_secure': self.is_secure,
            'secure_redirect_url': self.secure_redirect_url,
            'is_instant': self.is_instant,
            'instant_account_id': self.instant_account_id,
            'fee_account_id': self.fee_account_id,
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class CardPayinRefund:
    def __init__(self, card_payin_id, meta):
        """
        :param card_payin_id: string
        :param meta: Meta
        """
        self.card_payin_id = card_payin_id
        self.meta = meta

    def send(self):
        return {
            'card_payin_id': self.card_payin_id,
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class CardVerification:
    def __init__(self, card_info, card_token_id, card_id, is_secure, secure_redirect_url, meta=None):
        """
        :param card_info: CardInfo
        :param card_token_id: string
        :param card_id: string
        :param is_secure: boolean
        :param secure_redirect_url: string
        :param meta: Meta
        """
        self.card_info = card_info
        self.card_token_id = card_token_id
        self.card_id = card_id
        self.is_secure = is_secure
        self.secure_redirect_url = secure_redirect_url
        self.meta = meta

    def send(self):
        return {
            'card_info': self.card_info,
            'card_token_id': self.card_token_id,
            'card_id': self.card_id,
            'is_secure': self.is_secure,
            'secure_redirect_url': self.secure_redirect_url,
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class BankAccount:
    def __init__(self, bank_account_info, bank_info, customer_id, meta=None):
        """
        :param bank_account_info: BankAccountInfo
        :param bank_info: BankInfo
        :param customer_id: string
        :param meta: Meta
        """
        self.bank_account_info = bank_account_info
        self.bank_info = bank_info
        self.customer_id = customer_id
        self.meta = meta

    def send(self):
        return {
            'bank_account_info': self.bank_account_info,
            'bank_info': self.bank_info,
            'customer_id': self.customer_id,
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class BankPayin:
    def __init__(self, meta):
        """
        :param meta: Meta
        """
        self.meta

    def patch(self):
        return {
            'meta': self.meta
        }


class BankPayinReference:
    def __init_(self, account_id, meta=None):
        """
        :param account_id: string
        :param meta: Meta
        """
        self.account_id = account_id
        self.meta = meta

    def send(self):
        return {
            'account_id': self.account_id,
            'meta': self.meta
        }

    def patch(self):
        return self.send()


class BankPayout:
    def __init__(self, account_id, bank_account_id, bank_account_info, concept, value, meta=None):
        """
        :param account_id: string
        :param bank_account_id: string
        :param bank_account_info: BankAccountInfo
        :param concept: string
        :param value: Value
        :param meta: Meta
        """
        self.account_id = account_id
        self.bank_account_id = bank_account_id
        self.bank_account_info = bank_account_info
        self.concept = concept
        self.value = value
        self.meta = meta

    def send(self):
        return {
            'account_id': self.account_id,
            'bank_account_id': self.bank_account_id,
            'bank_account_info': self.bank_account_info,
            'concept': self.concept,
            'value': self.value,
            'meta': self.meta
        }

    def patch(self):
        return {
            'meta': self.meta
        }


class File:
    def __init__(self, public, file):
        """
        :param public: boolean
        :param file: bytes
        """
        self.public = public
        self.file = file

    def send(self):
        data = {
            'public': self.public,
            'file': self.file
        }
        return data


class Webhook:
    def __init__(self, url, enabled, triggers):
        """
        :param url: string
        :param enabled: boolean
        :param triggers: Trigger
        """
        self.url = url
        self.enabled = enabled
        self.triggers = triggers

    def send(self):
        return {
            'url': self.url,
            'enabled': self.enabled,
            'triggers': self.triggers
        }

    def patch(self):
        return self.send()


class Trigger:
    def __init__(self, card_payin_settled, auto_bank_payout_executed, bank_payout_started, bank_payin_completed):
        """
        :param card_payin_settled: boolean
        :param auto_bank_payout_executed: boolean
        :param bank_payout_started: boolean
        :param bank_payin_completed: boolean
        """
        self.card_payin_settled = card_payin_settled
        self.auto_bank_payout_executed = auto_bank_payout_executed
        self.bank_payout_started = bank_payout_started
        self.bank_payin_completed = bank_payin_completed

    def send(self):
        data = {
            'card_payin_settled': self.card_payin_settled,
            'auto_bank_payout_executed': self.auto_bank_payout_executed,
            'bank_payout_started': self.bank_payout_started,
            'bank_payin_completed': self.bank_payin_completed
        }
        return data
