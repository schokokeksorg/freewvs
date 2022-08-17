# freewvs

A local web vulnerability scanner.

freewvs is a tool to search webroots for know vulnerable versions of web applications.

## install

Install

You can install [freewvs via pip](https://pypi.org/project/freewvs/):

```
pip install freewvs
```

Alternatively you can run freewvs directly from the git source.

If you install via pip you need to update the freewvs database first:

```
update-freewvsdb
```

## usage

Just run freewvs with a path, e.g.:

```
freewvs /var/www
```

The output will be something like this:

```
Joomla 3.9.11 (3.9.14) CVE-2019-19846 /var/www/example.org
nextcloud 14.0.1 (14.0.5) CVE-2019-5449 /var/www/cloud.example.org
MediaWiki 1.31.1 (1.31.6) CVE-2019-19709 /var/www/wiki.example.org
```

## faq

#### What does freewvs do?

It scans your webroot for known vulnerable versions of popular web applications.

#### What does the output tell me?

Output looks like this:

```
Joomla-3 3.9.11 (3.9.13) CVE-2019-18674 /home/joe/websites/joessite/
```

This says that in /home/joe/websites/joessite/, there's a Joomla installation of version 3.9.11. This version is
vulnerable to CVE-2019-18674 and you should update to version 3.9.13.

#### CVE-2019-XXXX seems to be very minor, at least it doesn't affect me. Am I safe?

No, as freewvs only checks for the latest vulnerabilities. There may be other vulnerabilities in your version not listed by freewvs. The only way to be sure is to check the upstream changelog.

#### There is no version inside the brackets, what does that mean?

It means your web application has not released a security update. Often this means the software is no longer developed.

## contributions

See [CONTRIBUTIONS.md](CONTRIBUTIONS.md).

## misc

freewvs was developed by [schokokeks.org hosting](https://schokokeks.org/).

It's licensed under the 0BSD license.

https://freewvs.schokokeks.org
