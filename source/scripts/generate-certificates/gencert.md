# gencert.sh for Mattermost

```{include} ../../_static/badges/all-commercial.md
```

Generate a self-signed x509v3 certificate for use with multiple URLs / IPs. See the [configure SAML 2.0 with Okta for Mattermost](https://docs.mattermost.com/administration-guide/onboard/sso-saml-okta.html#before-you-begin) documentation for details on generating encryption certificates for encrypting the SAML connection.

## Generate Certificates

### Default values

```bash
CRT_CN="client.com" CRT_SAN="DNS.1:www.client.com,DNS.2:admin.client.com,IP.1:192.168.1.10,IP.2:10.0.0.234" gencert.sh
```

### Custom values

You may change the `CRT_CN` and `CRT_SAN` values of the above command based on your needs.

Additionally you may use any of the following environment variables :
- `CRT_FILENAME`: the name of the cert and key files i.e. `<CRT_FILENAME>.key` and `<CRT_FILENAME>.crt`
- `CRT_C` : Country value
- `CRT_L` : Locality value
- `CRT_O` : Organization value
- `CRT_OU` : Organizational Unit value
- `CRT_CN` : Common Name value
- `CRT_SAN` : SubjectAltName value

### Result

The command will generate two files:
- pkcs#8 private key : `mattermost-x509.key` (unless you set `CRT_FILENAME`)
- x509v3 certificate : `mattermost-x509.crt` (unless you set `CRT_FILENAME`)

You can confirm the certificate content by using the following standard `x509` command:

```bash
openssl x509 -in mattermost-x509.crt -noout -text
```

## Secure/Unsecure Certificates

The generated private key is passwordless by default. 

You can secure/unsecure the certificates using standard `pkcs8` commands:

```bash
# secure
openssl pkcs8 -in mattermost-x509.key -topk8 -v2 des3 -out mattermost-x509.secure.key

# unsecure
openssl pkcs8 -in mattermost-x509.secure.key -topk8 -nocrypt -out mattermost-x509.key
```

## Additional Reading

Below are additional guides and documentation for optional reading:
- [SubjectAltName page on wikipedia](https://en.wikipedia.org/wiki/SubjectAltName)
