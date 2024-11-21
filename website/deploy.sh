aws s3 sync . s3://procurement-negotiator
aws cloudfront create-invalidation --distribution-id  E1THD51BM99XCS --paths "/**/*" "/*"