# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHRraW50ZXIKaW1wb3J0IHN1YnByb2Nlc3MKZnJvbSB0a2ludGVyIGltcG9ydCAqCmZyb20gdGtpbnRlciBpbXBvcnQgZmlsZWRpYWxvZwppbXBvcnQgdGtpbnRlciBhcyB0awpmcm9tIHRraW50ZXIgaW1wb3J0IG1lc3NhZ2Vib3gKaW1wb3J0IHRraW50ZXIuZm9udCBhcyBmb250CmZyb20gUElMIGltcG9ydCBJbWFnZVRrLCBJbWFnZQppbXBvcnQgdXJsbGliLnJlcXVlc3QKZnJvbSBpbyBpbXBvcnQgQnl0ZXNJTwppbXBvcnQgb3MKaW1wb3J0IGlvCmltcG9ydCBzeXMKaW1wb3J0IHBpY2tsZQppbXBvcnQgdGltZQpmcm9tIGRlY2ltYWwgaW1wb3J0ICoKaW1wb3J0IHdlYmJyb3dzZXIKZnJvbSBzZWxlbml1bSBpbXBvcnQgd2ViZHJpdmVyCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNvbW1vbi5ieSBpbXBvcnQgQnkKZnJvbSBzZWxlbml1bS53ZWJkcml2ZXIuc3VwcG9ydC53YWl0IGltcG9ydCBXZWJEcml2ZXJXYWl0CmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLmNocm9tZS5vcHRpb25zIGltcG9ydCBPcHRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQgaW1wb3J0IGV4cGVjdGVkX2NvbmRpdGlvbnMgYXMgRXhwZWN0ZWRDb25kaXRpb25zCmZyb20gc2VsZW5pdW0ud2ViZHJpdmVyLnN1cHBvcnQudWkgaW1wb3J0IFNlbGVjdAppbXBvcnQganNvbgppbXBvcnQgc3NsCmltcG9ydCBjZXJ0aWZpCgpmcm9tIENTViBpbXBvcnQgQ1NWCmZyb20gSlNPTiBpbXBvcnQgSlNPTgpmcm9tIE5GVCBpbXBvcnQgTkZUCgoKcm9vdCA9IFRrKCkKCnJvb3QuZ2VvbWV0cnkoJzc1MHg3NTAnKQpyb290LnJlc2l6YWJsZShGYWxzZSwgRmFsc2UpCnJvb3QudGl0bGUoIk5GVHMgVXBsb2FkIHRvIE9wZW5TZWEgdjEuMCIpCiAgCmlucHV0X3NhdmVfbGlzdCA9IFsiTkZUcyBmb2xkZXIgOiIsIDAsIDAsIDAsIDAsIDAsIDAsIDAsIDBdCm1haW5fZGlyZWN0b3J5ID0gb3MucGF0aC5qb2luKHN5cy5wYXRoWzBdKQoKCmRlZiBzdXBwb3J0VVJMKCk6CiAgICB3ZWJicm93c2VyLm9wZW5fbmV3KCJodHRwczovL3d3dy5pbmZvdHJleC5uZXQvb3BlbnNlYS9zdXBwb3J0LmFzcD9yPWFwcCIpCgoKY2xhc3MgV2ViSW1hZ2U6CiAgICBkZWYgX19pbml0X18oc2VsZiwgdXJsKToKICAgICAgICB3aXRoIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4odXJsLCBjb250ZXh0PXNzbC5jcmVhdGVfZGVmYXVsdF9jb250ZXh0KGNhZmlsZT1jZXJ0aWZpLndoZXJlKCkpKSBhcyB1OgogICAgICAgICAgICByYXdfZGF0YSA9IHUucmVhZCgpCiAgICAgICAgI3NlbGYuaW1hZ2UgPSB0ay5QaG90b0ltYWdlKGRhdGE9YmFzZTY0LmVuY29kZWJ5dGVzKHJhd19kYXRhKSkKICAgICAgICBpbWFnZSA9IEltYWdlLm9wZW4oaW8uQnl0ZXNJTyhyYXdfZGF0YSkpCiAgICAgICAgc2VsZi5pbWFnZSA9IEltYWdlVGsuUGhvdG9JbWFnZShpbWFnZSkKCiAgICBkZWYgZ2V0KHNlbGYpOgogICAgICAgIHJldHVybiBzZWxmLmltYWdlCmltYWdldXJsID0gImh0dHBzOi8vd3d3LmluZm90cmV4Lm5ldC9vcGVuc2VhL2hlYWRlci5wbmciCmltZyA9IFdlYkltYWdlKGltYWdldXJsKS5nZXQoKQppbWFnZWxhYiA9IHRrLkxhYmVsKHJvb3QsIGltYWdlPWltZykKaW1hZ2VsYWIuZ3JpZChyb3c9MCwgY29sdW1uc3Bhbj0yKQppbWFnZWxhYi5iaW5kKCI8QnV0dG9uLTE+IiwgbGFtYmRhIGU6c3VwcG9ydFVSTCgpKQoKaXNfcG9seWdvbiA9IEJvb2xlYW5WYXIoKQppc19wb2x5Z29uLnNldChGYWxzZSkgCgpkZWYgb3Blbl9jaHJvbWVfcHJvZmlsZSgpOgogICAgc3VicHJvY2Vzcy5Qb3BlbigKICAgICAgICBbCiAgICAgICAgICAgICJzdGFydCIsCiAgICAgICAgICAgICJjaHJvbWUiLAogICAgICAgICAgICAiLS1yZW1vdGUtZGVidWdnaW5nLXBvcnQ9ODk4OSIsCiAgICAgICAgICAgICItLXVzZXItZGF0YS1kaXI9IiArIG1haW5fZGlyZWN0b3J5ICsgIi9jaHJvbWVfcHJvZmlsZSIsCiAgICAgICAgXSwKICAgICAgICBzaGVsbD1UcnVlLAogICAgKQoKCmRlZiBzYXZlX2ZpbGVfcGF0aCgpOgogICAgI3JldHVybiBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0sICJTYXZlX2ZpbGUuY2xvdWQiKSAKICAgIHJldHVybiBvcy5wYXRoLmpvaW4oc3lzLnBhdGhbMF0sICJTYXZlX2d1aS5jbG91ZCIpIAoKCiMgYXNrIGZvciBkaXJlY3Rvcnkgb24gY2xpY2tpbmcgYnV0dG9uLCBjaGFuZ2VzIGJ1dHRvbiBuYW1lLgpkZWYgdXBsb2FkX2ZvbGRlcl9pbnB1dCgpOgogICAgZ2xvYmFsIHVwbG9hZF9wYXRoCiAgICB1cGxvYWRfcGF0aCA9IGZpbGVkaWFsb2cuYXNrZGlyZWN0b3J5KCkKICAgIE5hbWVfY2hhbmdlX2ltZ19mb2xkZXJfYnV0dG9uKHVwbG9hZF9wYXRoKQoKZGVmIE5hbWVfY2hhbmdlX2ltZ19mb2xkZXJfYnV0dG9uKHVwbG9hZF9mb2xkZXJfaW5wdXQpOgogICAgdXBsb2FkX2ZvbGRlcl9pbnB1dF9idXR0b25bInRleHQiXSA9IHVwbG9hZF9mb2xkZXJfaW5wdXQKCmRlZiBpc19udW1lcmljKHZhbCk6CglpZiBzdHIodmFsKS5pc2RpZ2l0KCk6CgkJcmV0dXJuIFRydWUKCWVsaWYgc3RyKHZhbCkucmVwbGFjZSgnLicsJycsMSkuaXNkaWdpdCgpOgoJCXJldHVybiBUcnVlCgllbHNlOgoJCXJldHVybiBGYWxzZQoKY2xhc3MgSW5wdXRGaWVsZDoKICAgIGRlZiBfX2luaXRfXyhzZWxmLCBsYWJlbCwgcm93X2lvLCBjb2x1bW5faW8sIHBvcywgIG1hc3Rlcj1yb290KToKICAgICAgICBzZWxmLm1hc3RlciA9IG1hc3RlcgogICAgICAgIHNlbGYuaW5wdXRfZmllbGQgPSBFbnRyeShzZWxmLm1hc3Rlciwgd2lkdGg9NjApCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5ncmlkKGlwYWR5PTMpCiAgICAgICAgc2VsZi5pbnB1dF9maWVsZC5sYWJlbCA9IExhYmVsKG1hc3RlciwgdGV4dD1sYWJlbCwgYW5jaG9yPSJ3Iiwgd2lkdGg9MjAsIGhlaWdodD0xICkKICAgICAgICBzZWxmLmlucHV0X2ZpZWxkLmxhYmVsLmdyaWQocm93PXJvd19pbywgY29sdW1uPWNvbHVtbl9pbywgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHNlbGYuaW5wdXRfZmllbGQuZ3JpZChyb3c9cm93X2lvLCBjb2x1bW49Y29sdW1uX2lvICsgMSwgcGFkeD0xMiwgcGFkeT0yKQogICAgICAgIHRyeToKICAgICAgICAgICAgd2l0aCBvcGVuKHNhdmVfZmlsZV9wYXRoKCksICJyYiIpIGFzIGluZmlsZToKICAgICAgICAgICAgICAgIG5ld19kaWN0ID0gcGlja2xlLmxvYWQoaW5maWxlKQogICAgICAgICAgICAgICAgc2VsZi5pbnNlcnRfdGV4dChuZXdfZGljdFtwb3NdKQogICAgICAgIGV4Y2VwdCBGaWxlTm90Rm91bmRFcnJvcjoKICAgICAgICAgICAgcGFzcwogICAgICAgIAogICAgZGVmIGluc2VydF90ZXh0KHNlbGYsIHRl'
love = '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'
god = 'cmljZS5pbnB1dF9maWVsZC5nZXQoKSkKICAgIGxvb3BfdGl0bGUgPSB0aXRsZS5pbnB1dF9maWVsZC5nZXQoKQogICAgbG9vcF9maWxlX2Zvcm1hdCA9IGZpbGVfZm9ybWF0LmlucHV0X2ZpZWxkLmdldCgpCiAgICBsb29wX2V4dGVybmFsX2xpbmsgPSBzdHIoZXh0ZXJuYWxfbGluay5pbnB1dF9maWVsZC5nZXQoKSkKICAgIGxvb3BfZGVzY3JpcHRpb24gPSBkZXNjcmlwdGlvbi5pbnB1dF9maWVsZC5nZXQoKQoKICAgICMjY2hyb21lb3B0aW9ucwogICAgb3B0ID0gT3B0aW9ucygpCiAgICBvcHQuYWRkX2V4cGVyaW1lbnRhbF9vcHRpb24oImRlYnVnZ2VyQWRkcmVzcyIsICJsb2NhbGhvc3Q6ODk4OSIpCiAgICBkcml2ZXIgPSB3ZWJkcml2ZXIuQ2hyb21lKAogICAgICAgIGV4ZWN1dGFibGVfcGF0aD1wcm9qZWN0X3BhdGggKyAiL2Nocm9tZWRyaXZlci5leGUiLAogICAgICAgIGNocm9tZV9vcHRpb25zPW9wdCwKICAgICkKICAgIHdhaXQgPSBXZWJEcml2ZXJXYWl0KGRyaXZlciwgNjApCgogICAgIyMjd2FpdCBmb3IgbWV0aG9kcwogICAgZGVmIHdhaXRfY3NzX3NlbGVjdG9yKGNvZGUpOgogICAgICAgIHdhaXQudW50aWwoCiAgICAgICAgICAgIEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoKEJ5LkNTU19TRUxFQ1RPUiwgY29kZSkpCiAgICAgICAgKQogICAgICAgIAogICAgZGVmIHdhaXRfY3NzX3NlbGVjdG9yVGVzdChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKAogICAgICAgICAgICBFeHBlY3RlZENvbmRpdGlvbnMuZWxlbWVudFRvQmVDbGlja2FibGUoKEJ5LkNTU19TRUxFQ1RPUiwgY29kZSkpCiAgICAgICAgKSAgICAKCiAgICBkZWYgd2FpdF94cGF0aChjb2RlKToKICAgICAgICB3YWl0LnVudGlsKEV4cGVjdGVkQ29uZGl0aW9ucy5wcmVzZW5jZV9vZl9lbGVtZW50X2xvY2F0ZWQoKEJ5LlhQQVRILCBjb2RlKSkpCgoKICAgIHdoaWxlIGVuZF9udW0gPj0gc3RhcnRfbnVtOgogICAgICAgIHByaW50KCJTdGFydCBjcmVhdGluZyBORlQgIiArICBsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpCiAgICAgICAgcHJpbnQoJ251bWJlciAnLCAgc3RhcnRfbnVtKQogICAgICAgIGRyaXZlci5nZXQoY29sbGVjdGlvbl9saW5rKQoKICAgICAgICB3YWl0X3hwYXRoKCcvLypbQGlkPSJtZWRpYSJdJykKICAgICAgICBpbWFnZVVwbG9hZCA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9Im1lZGlhIl0nKQogICAgICAgIGltYWdlUGF0aCA9IG9zLnBhdGguYWJzcGF0aChmaWxlX3BhdGggKyAiXFxpbWFnZXNcXCIgKyBzdHIoc3RhcnRfbnVtKSArICIuIiArIGxvb3BfZmlsZV9mb3JtYXQpICAjIGNoYW5nZSBmb2xkZXIgaGVyZQogICAgICAgIGltYWdlVXBsb2FkLnNlbmRfa2V5cyhpbWFnZVBhdGgpCiAgICAgICAgdGltZS5zbGVlcCgyKQoKICAgICAgICBuYW1lID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy8qW0BpZD0ibmFtZSJdJykKICAgICAgICBuYW1lLnNlbmRfa2V5cyhsb29wX3RpdGxlICsgc3RyKHN0YXJ0X251bSkpICAjICsxMDAwIGZvciBvdGhlciBmb2xkZXJzICNjaGFuZ2UgbmFtZSBiZWZvcmUgIiMiCiAgICAgICAgdGltZS5zbGVlcCgyKQoKICAgICAgICBleHRfbGluayA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8vKltAaWQ9ImV4dGVybmFsX2xpbmsiXScpCiAgICAgICAgZXh0X2xpbmsuc2VuZF9rZXlzKGxvb3BfZXh0ZXJuYWxfbGluaykKICAgICAgICB0aW1lLnNsZWVwKDIpCgogICAgICAgIGRlc2MgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvLypbQGlkPSJkZXNjcmlwdGlvbiJdJykKICAgICAgICBkZXNjLnNlbmRfa2V5cyhsb29wX2Rlc2NyaXB0aW9uKQogICAgICAgIHRpbWUuc2xlZXAoMSkKCiAgICAgICAgI2pzb25EYXRhID0gSlNPTihmaWxlX3BhdGggKyAiL2pzb24vIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkRnJvbUZpbGUoKQoKICAgICAgICBqc29uRmlsZSA9IGZpbGVfcGF0aCArICIvanNvbi8iKyBzdHIoc3RhcnRfbnVtKSArICIuanNvbiIKICAgICAgICBpZiBvcy5wYXRoLmlzZmlsZShqc29uRmlsZSkgYW5kIG9zLmFjY2Vzcyhqc29uRmlsZSwgb3MuUl9PSyk6CiAgICAgICAgICAgCiAgICAgICAgICAgICNwcmludChzdHIoanNvbk1ldGFEYXRhKSkKICAgICAgICAgICAgd2FpdF9jc3Nfc2VsZWN0b3IoImJ1dHRvblthcmlhLWxhYmVsPSdBZGQgcHJvcGVydGllcyddIikKICAgICAgICAgICAgcHJvcGVydGllcyA9IGRyaXZlci5maW5kX2VsZW1lbnRfYnlfY3NzX3NlbGVjdG9yKCJidXR0b25bYXJpYS1sYWJlbD0nQWRkIHByb3BlcnRpZXMnXSIpCiAgICAgICAgICAgIGRyaXZlci5leGVjdXRlX3NjcmlwdCgiYXJndW1lbnRzWzBdLmNsaWNrKCk7IiwgcHJvcGVydGllcykKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQoKICAgICAgICAgICAgIyBqc29uRGF0YSA9IEpTT04ob3MuZ2V0Y3dkKCkgKyAiL2RhdGEvIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkRnJvbUZpbGUoKQogICAgICAgICAgICAjIGpzb25NZXRhRGF0YSA9IGpzb25EYXRhWydhdHRyaWJ1dGVzJ10KCiAgICAgICAgICAgICAjIGNoZWNrcyBpZiBmaWxlIGV4aXN0cwogICAgICAgICAgICBqc29uRGF0YSA9IGpzb24ubG9hZHMob3BlbihmaWxlX3BhdGggICsgIlxcanNvblxcIisgc3RyKHN0YXJ0X251bSkgKyAiLmpzb24iKS5yZWFkKCkpCiAgICAgICAgICAgIGpzb25NZXRhRGF0YSA9IGpzb25EYXRhWydhdHRyaWJ1dGVzJ10KCiAgICAgICAgICAgIGZvciBrZXkgaW4ganNvbk1ldGFEYXRhOgogICAgICAgICAgICAgICAgaW5wdXQxID0gZHJpdmVyLmZpbmRfZWxlbWVudF9ieV94cGF0aCgnLy90Ym9keVtAY2xhc3M9IkFzc2V0VHJhaXRzRm9ybS0tYm9keSJdL3RyW2xhc3QoKV0vdGRbMV0vZGl2L2Rpdi9pbnB1dCcpCiAgICAgICAgICAgICAgICBpbnB1dDIgPSBkcml2ZXIuZmluZF9lbGVtZW50X2J5X3hwYXRoKCcvL3Rib2R5W0BjbGFzcz0iQXNzZXRUcmFpdHNGb3JtLS1ib2R5Il0vdHJbbGFzdCgpXS90ZFsyXS9kaXYvZGl2L2lucHV0JykKICAgICAgICAgICAgICAgICNwcmludChzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgI3ByaW50KHN0cihrZXlbJ3ZhbHVlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQxLnNlbmRfa2V5cyhzdHIoa2V5Wyd0cmFpdF90eXBlJ10pKQogICAgICAgICAgICAgICAgaW5wdXQyLnNlbmRfa2V5cyhzdHIoa2V5Wyd2YWx1ZSddKSkKICAgICAgICAgICAgICAgIGRyaXZlci5maW5kX2VsZW1lbnRfYnlfeHBhdGgoJy8v'
destiny = 'LaI0qT9hJ3EyrUDbXG0vDJExVT1ipzHvKFpcYzAfnJAeXPxXVPNtVPNtVPNtVPNtVPNtVUEcoJHhp2kyMKNbZFxXPvNtVPNtVPNtVPNtVTElnKMypv5znJ5xK2IfMJ1yoaEsLaysrUOuqTtbWl8iLaI0qT9hJ3EyrUDbXG0vH2S2MFWqWlxhL2kcL2fbXDbtVPNtVPNtVPNtVPO0nJ1yYaAfMJIjXQRcPtbtVPNtVPNtVPZtH2IfMJA0VSOioUyao24tLzkiL2gwnTScovOcMvOupUOfnJAuLzkyPvNtVPNtVPNtnJLtnKAspT9frJqiov5aMKDbXGbXVPNtVPNtVPNtVPNtLzkiL2gwnTScoy9vqKE0o24tCFOxpzy2MKVhMzyhMS9yoTIgMJ50XRW5YyuDDIEVYPNaYl8dJ0OcMQ0vK19hMKu0Vy0iMTy2JmSqY21unJ4iMTy2Y2Ecqv9mMJA0nJ9hY2Ecqv9zo3WgY2Ecqyf3KF9xnKLiMTy2JmWqWlxXVPNtVPNtVPNtVPNtLzkiL2gwnTScoy9vqKE0o24hL2kcL2fbXDbtVPNtVPNtVPNtVPOjo2k5M29hK2W1qUEioy9fo2AuqTyiovN9VPpiY3AjLJ5ooz9loJSfnKcyYKAjLJAyXPxtCFNvGKIgLzScVy0aPvNtVPNtVPNtVPNtVUqunKDhqJ50nJjbEKujMJA0MJEQo25xnKEco25mYaOlMKAyozAyK29zK2IfMJ1yoaEsoT9wLKEyMPtXVPNtVPNtVPNtVPNtVPNtVPuPrF5LHRSHFPjtpT9frJqioy9vqKE0o25soT9wLKEco24cXFxXVPNtVPNtVPNtVPNtpT9frJqioy9vqKE0o24tCFOxpzy2MKVhMzyhMS9yoTIgMJ50XNbtVPNtVPNtVPNtVPNtVPNtDaxhJSOOIRtfVUOioUyao25sLaI0qT9hK2kiL2S0nJ9hXDbtVPNtVPNtVPNtVPOjo2k5M29hK2W1qUEiov5woTywnltcPtbXVPNtVPNtVPOwpzIuqTHtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K3ujLKEbXPpiYlcoDTyxCFWsK25yrUDvKF9xnKMoZI0ioJScov9xnKLiMTy2Y3AyL3Eco24iMTy2JmWqY2Mipz0iMTy2Y2EcqyfkKF9mpTShY2W1qUEiovpcPvNtVPNtVPNtMUWcqzIlYzI4MJA1qTIsp2AlnKO0XPWupzq1oJIhqUAoZS0hL2kcL2fbXGfvYPOwpzIuqTHcPvNtVPNtVPNtqTygMF5moTIypPtkXDbXVPNtVPNtVPO3LJy0K2Amp19mMJkyL3EipvtvnIgupzyuYJkuLzIfCFqQoT9mMFqqVvxXVPNtVPNtVPOwpz9mplN9VTElnKMypv5znJ5xK2IfMJ1yoaEsLaysL3AmK3AyoTIwqT9lXPWcJ2SlnJRgoTSvMJj9W0Afo3AyW10vXDbtVPNtVPNtVTAlo3AmYzAfnJAeXPxXVPNtVPNtVPO0nJ1yYaAfMJIjXQRcPtbtVPNtVPNtVT1unJ5spTSaMFN9VTElnKMypv5wqKWlMJ50K3qcozEiq19bLJ5xoTHXVPNtVPNtVPO3LJy0K3ujLKEbXPpiYlcoDTyxCFWsK25yrUDvKF9xnKMoZI0ioJScov9xnKLiMTy2Y2EcqyfkKF9xnKLip3OuoyflKF9uWlxXVPNtVPNtVPOmMJkfVQ0tMUWcqzIlYzMcozEsMJkyoJIhqS9vrI94pTS0nPtaYl8dJ0OcMQ0vK19hMKu0Vy0iMTy2JmSqY21unJ4iMTy2Y2Ecqv9xnKMoZI0iMTy2Y3AjLJ5oZy0iLFpcPvNtVPNtVPNtp2IfoP5woTywnltcPtbXVPNtVPNtVPO3LJy0K2Amp19mMJkyL3EipvtvnJ5jqKEopTkuL2Ibo2kxMKV9W0Sgo3IhqPqqVvxXVPNtVPNtVPOuoJ91oaDtCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K2Amp19mMJkyL3EipvtvnJ5jqKEopTkuL2Ibo2kxMKV9W0Sgo3IhqPqqVvxXVPNtVPNtVPOuoJ91oaDhp2IhMS9eMKymXUA0pvufo29jK3OlnJAyXFxXVPNtVPNtVPO0nJ1yYaAfMJIjXQRcPtbtVPNtVPNtVUqunKEsL3AmK3AyoTIwqT9lXPWvqKE0o25oqUyjMG0ap3IvoJy0W10vXDbtVPNtVPNtVTkcp3EcozptCFOxpzy2MKVhMzyhMS9yoTIgMJ50K2W5K2Amp19mMJkyL3EipvtvLaI0qT9hJ3E5pTH9W3A1Lz1cqPqqVvxXVPNtVPNtVPOfnKA0nJ5aYzAfnJAeXPxXVPNtVPNtVPO0nJ1yYaAfMJIjXQDcPtbXVPNt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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))