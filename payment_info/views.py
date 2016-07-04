# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'redemption_code': participant.label or participant.code,
            'payoff': participant.vars["carrying_payoff"],
            'apoints': participant.vars["ravens_points"]
        }


page_sequence = [PaymentInfo]
