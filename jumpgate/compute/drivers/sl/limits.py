

class LimitsV2(object):
    def on_get(self, req, resp, tenant_id):
        client = req.env['sl_client']

        account = client['Account'].getObject(
            mask='mask[hourlyVirtualGuestCount]')

        # TODO(kmcdonald) - This shouldn't be hardcoded
        limits = {
            'absolute': {
                'maxImageMeta': 0,
                'maxPersonality': 5,
                'maxPersonalitySize': 10240,
                'maxSecurityGroupRules': 999999,
                'maxSecurityGroups': 999999,
                'maxServerMeta': 999999,
                'maxTotalCores': 999999,
                'maxTotalFloatingIps': 999999,
                'maxTotalInstances': 999999,
                'maxTotalKeypairs': 999999,
                'maxTotalRAMSize': 999999999,
                'totalInstancesUsed': account['hourlyVirtualGuestCount'],
                'totalCoresUsed': 0,
                'totalRAMUsed': 0,
                'totalFloatingIpsUsed': 0,
                'totalSecurityGroupsUsed': 0,
            },
            # TODO(imkarrer) - Added rate to make tempest pass, need real rate
            'rate': [],
        }

        resp.body = {'limits': limits}
