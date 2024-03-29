from odoo.tests import common


class TestAttachExistingAttachment(common.TransactionCase):
    def setUp(self):
        super().setUp()
        self.partner_obj = self.env["res.partner"]
        self.partner_01 = self.env.ref("base.res_partner_10")
        self.partner_02 = self.env.ref("base.res_partner_address_17")

    def test_send_email_attachment(self):
        ctx = self.env.context.copy()
        ctx.update(
            {
                "default_model": "res.partner",
                "default_res_id": self.partner_01.id,
                "default_composition_mode": "comment",
            }
        )
        mail_compose = self.env["mail.compose.message"]
        values = mail_compose.with_context(ctx).onchange_template_id(
            False, "comment", "res.partner", self.partner_01.id
        )["value"]
        values["partner_ids"] = [(4, self.partner_02.id)]
        compose_id = mail_compose.with_context(ctx).create(values)
        compose_id.send_mail()
        res = self.env["mail.followers"].search(
            [
                ("res_model", "=", "res.partner"),
                ("res_id", "=", self.partner_01.id),
                ("partner_id", "=", self.partner_02.id),
            ]
        )
        # I check if the recipient isn't a follower
        self.assertEqual(len(res.ids), 0)
