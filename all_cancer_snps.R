library(TwoSampleMR)
ao = available_outcomes()
#cancer_ids = c('ieu-a-1126', 'ieu-a-1120', 'ukb-d-C_SKIN', 'ukb-d-C_DIGESTIVE_ORGANS', 'ukb-b-12915', 'ieu-a-965', 'ieu-a-1013', 'ukb-d-C_URINARY_TRACT', 'ieu-a-816')
cancer_ids = c('ieu-a-1128', 'ieu-a-1127', 'ieu-a-1126')
ao_subset = ao[is.element(ao$id, cancer_ids),]

all_snps_associated = c()
for (id in cancer_ids[3]) {
  print(id)
  associated_instruments = extract_instruments(id)
  all_snps_associated = c(all_snps_associated, associated_instruments$SNP)
}
all_snps_associated = unique(all_snps_associated)

all_snps_cancers = data.frame('SNP'=all_snps_associated)
for (id in cancer_ids) {
  cancer_name = as.character(ao[ao$id == id,'trait']) 
  effect_of_snps = extract_outcome_data(all_snps_cancers$SNP, id)
  effect_of_snps = effect_of_snps[, c('SNP', 'beta.outcome', 'se.outcome', 'pval.outcome')] 
  names(effect_of_snps) = c('SNP', paste0('beta.', cancer_name), paste0('se.', cancer_name), paste0('pval.', cancer_name))
  all_snps_cancers = merge(all_snps_cancers, effect_of_snps, by='SNP', all.x = TRUE)
}
write.csv(all_snps_cancers, 'all_snps_cancers.csv', row.names = F, quote=F)
